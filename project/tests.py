import unittest
import sqlite3
import os
import pandas as pd

class SystemTest(unittest.TestCase):

    def setUp(self):
        git_repo_root = os.path.dirname(os.path.abspath(__file__))
        merged_data_path = f'made-template/data/merged_data.csv'
        df_merged = pd.read_csv(merged_data_path)

        merged_data_db_path = f'made-template/data/merged_data.db'
        conn = sqlite3.connect(merged_data_db_path)
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
        cursor.close()
        conn.close()

    def test_db_file_exists(self):
        # The database file should be created by the data pipeline
        db_file = 'merged_data.db'

        # Verify that the database file exists
        self.assertTrue(os.path.exists(db_file))

    def test_tables_exist(self):
        # Connect to the database file
        conn = sqlite3.connect('merged_data.db')
        cursor = conn.cursor()

        # Get a list of tables in the database
        tables = cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')

        # Verify that the expected tables exist
        expected_tables = ['merged_data']

        for expected_table in expected_tables:
            # Check if the expected table exists in the list of tables
            self.assertIn(expected_table, tables.fetchall())

        # Close the connection to the database
        cursor.close()
        conn.close()

    def test_output_files_exist(self):
        # The output files should be created by the data pipeline
        output_files = ['merged_data.db']

        for output_file in output_files:
            # Verify that the output file exists
            self.assertTrue(os.path.exists(output_files))

if __name__ == '__main__':
    unittest.main()
