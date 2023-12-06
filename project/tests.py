import unittest
import pandas as pd
import sqlite3
import os

# Define the connection parameters for the SQLite database
db_path = 'data/FEU_profit_loss_data.db'

class DataPipelineTests(unittest.TestCase):

    def test_data_exists(self):
        # Check if the SQLite database exists
        if not os.path.exists(db_path):
            raise Exception('The SQLite database file does not exist.')

    def test_data_integrity(self):
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)

        # Check the content of the 'profit_loss_data' table
        cur = conn.cursor()
        cur.execute('SELECT year, quarter, profit_loss FROM profit_loss_data')
        profit_loss_data = cur.fetchall()

        # Check that there are two rows in the table
        if len(profit_loss_data) != 2:
            raise Exception('The SQLite database should contain 2 rows, but it contains $num_rows rows.')

        # Close the connection to the SQLite database
        conn.close()

if __name__ == '__main__':
    unittest.main()
