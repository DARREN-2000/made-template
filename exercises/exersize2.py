import pandas as pd
import sqlite3
import requests

# URL for the dataset
url_dataset = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"

# Function to fetch data
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch data. Check the URL.")
        return None

# Fetch data
data = fetch_data(url_dataset)

if data:
    # Load dataset into a Pandas DataFrame
    try:
        # Read CSV with ';' as delimiter and specific column names
        df = pd.read_csv(url_dataset, encoding='latin1', sep=';', names=['EVA_NR', 'DS100', 'IFOPT', 'NAME', 'Verkehr', 'Laenge', 'Breite', 'Betreiber_Name', 'Betreiber_Nr', 'Status'], on_bad_lines='skip')
        
        # Drop the "Status" column
        df.drop(columns=['Status'], inplace=True, errors='ignore')

        # Check for valid columns in the DataFrame
        if 'Verkehr' in df.columns and 'Laenge' in df.columns and 'Breite' in df.columns:
            # Convert 'Laenge' and 'Breite' columns to numeric (errors='coerce' will turn non-numeric values to NaN)
            df['Laenge'] = pd.to_numeric(df['Laenge'], errors='coerce')
            df['Breite'] = pd.to_numeric(df['Breite'], errors='coerce')

            # Filter rows with valid values for "Verkehr", "Laenge", and "Breite"
            df = df[(df['Laenge'].between(-90, 90, inclusive='both')) & (df['Breite'].between(-90, 90, inclusive='both'))]

            # Connect to SQLite database and store the cleaned data
            conn = sqlite3.connect('trainstops.sqlite')  # Create/connect to SQLite database
            df.to_sql('trainstops', conn, index=False, if_exists='replace')  # Store data as a table in the database
            conn.close()  # Close connection to the database

            print("Data loaded and cleaned, stored in trainstops.sqlite as 'trainstops' table.")
        else:
            print("Required columns not found in the dataset.")

    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}")
else:
    print("Failed to fetch data. Check the URL.")
