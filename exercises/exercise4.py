import os
import zipfile
import urllib.request
import pandas as pd
import sqlite3

# Data pipeline steps
pipeline_steps = []

print("Starting data pipeline...")
pipeline_steps.append("Imported libraries")

# Download and unzip the data
zip_file_url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
download_path = "mowesta-dataset.zip"
downloaded_csv = "mowesta-dataset"

urllib.request.urlretrieve(zip_file_url, download_path)
if os.path.exists(zip_file_url):
    if not os.path.exists(downloaded_csv):
        os.makedirs(download_path)
pipeline_steps.append("Downloaded and unzipped data")

# Extract the CSV file from the ZIP archive
with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extract("data.csv", path=".")
pipeline_steps.append("Extracted CSV file from ZIP archive")

# Set the file path to the extracted CSV file
file_path = os.path.join(downloaded_csv, "data.csv")

# Load the CSV file into a DataFrame, skip lines with errors
df = pd.read_csv(file_path, sep=";", decimal=",", index_col=False,usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)","Batterietemperatur in °C", "Geraet aktiv"])
pipeline_steps.append("Loaded data into a DataFrame")

# Rename columns
df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur",
                        "Batterietemperatur in °C": "Batterietemperatur"})

# Transform data: Convert temperatures to Fahrenheit
df["Temperatur"] = (df["Temperatur"] * 9/5) + 32
df["Batterietemperatur"] = (df["Batterietemperatur"] * 9/5) + 32
pipeline_steps.append("Converted temperatures to Fahrenheit")

# Validate data: Check if "Geraet" is an id over 0
df = df[df["Geraet"] > 0]

# Reshape data: Select only the specified columns with the new names
selected_columns = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur", "Batterietemperatur", "Geraet aktiv"]
df = df.loc[:, selected_columns]
pipeline_steps.append("Selected specific columns")

# Write data into SQLite database
# Write data into SQLite database
db_path = "temperatures.sqlite"
table_name = "temperatures"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
create_table_query = f"""
    CREATE TABLE IF NOT EXISTS temperatures (
    Geraet BIGINT,
    Hersteller TEXT,
    Model TEXT,
    Monat TEXT,
    Temperatur FLOAT,
    Batterietemperatur FLOAT,
    Geraet_aktiv TEXT)"""
cursor.execute(create_table_query)
df.to_sql('temperatures', conn, if_exists='replace', index=False)
conn.commit()
pipeline_steps.append("Sucessfully wrote data into SQLite database")

# Close the database connection
conn.close()

# Print pipeline summary
print("Data pipeline steps:")
for step in pipeline_steps:
    print(step)

print("Data pipeline completed successfully...")
# Run the script
# python exercise4.py