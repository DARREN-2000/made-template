import os
import sqlite3
import pandas as pd

# Create the `data` directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Load the datasets
df_g71811_0023 = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/71811-0023_00.csv', encoding='latin1', sep=';' )
df_g71811_0024 = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/71811-0024_00.csv', encoding='latin1',sep=';' )

# Create the database connection
conn = sqlite3.connect('data/FEU_profit_loss_data.db')

# Create the cursor object to execute SQL queries
cursor = conn.cursor()

# Drop the tables if they already exist
cursor.execute('DROP TABLE IF EXISTS g71811_0023')
cursor.execute('DROP TABLE IF EXISTS g71811_0024')

# Create the tables
cursor.execute("""CREATE TABLE g71811_0023 (
    Bundesland TEXT,
    Anzahl_zum_31122017 INTEGER,
    Jahr INTEGER
)""")
cursor.execute("""CREATE TABLE g71811_0024 (
    Bundesland TEXT,
    Anzahl_zum_31122022 INTEGER,
    Jahr INTEGER
)""")

# Insert the data into the tables
df_g71811_0023.to_sql('GENESIS-Tabelle: 71811-0023', conn, if_exists='append', index=False)
df_g71811_0024.to_sql('GENESIS-Tabelle: 71811-0024', conn, if_exists='append', index=False)



# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()

print('Successfully connected the two datasets into the SQLite database.')
