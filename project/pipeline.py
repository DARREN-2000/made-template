import pandas as pd
import sqlite3

# Load the merged data
df_merged = pd.read_csv(r"E:\GITHUB\PROGRAMMING\FAU\ADE\final\data\merged_data.csv")

# Create an SQLite database
conn = sqlite3.connect(r'e:\GITHUB\PROGRAMMING\FAU\ADE\final\data\merged_data.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table named 'merged_data'
create_table_statement = """
CREATE TABLE IF NOT EXISTS merged_data (
    Value_x INTEGER,
    Value_y INTEGER,
    Time INT,
    Series_Name_x TEXT,
    Series_Name_y TEXT,
    Country_Name_x TEXT,
    Country_Name_y TEXT
)
"""

cursor.execute(create_table_statement)

# Convert merged data to format compatible with SQLite
merged_data_values = df_merged.to_numpy()

# Insert the merged data into the 'merged_data' table
cursor.executemany('INSERT INTO merged_data (Value_x, Value_y, Time, Series_Name_x, Series_Name_y, Country_Name_x, Country_Name_y) VALUES (?, ?, ?, ?, ?, ?, ?)', merged_data_values)

# Commit the data to the database
conn.commit()

# Close the connection to the database
conn.close()
