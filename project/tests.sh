#!/bin/bash

# Install the required Python libraries
pip install pandas requests sqlite3

# Define the data pipeline script
data_pipeline_script=data_pipeline.py

# Execute the data pipeline script
python $data_pipeline_script

# Validate that the output file exists
if [ ! -f "data/FEU_profit_loss_data.db" ]; then
    echo "Error: The output file \"data/FEU_profit_loss_data.db\" does not exist."
    exit 1
fi

# Check the content of the SQLite database
conn = sqlite3.connect('data/FEU_profit_loss_data.db')
cur = conn.cursor()
cur.execute('SELECT year, quarter, profit_loss FROM profit_loss_data')
profit_loss_data = cur.fetchall()
if len(profit_loss_data) != 2:
    echo "Error: The SQLite database should contain 2 rows, but it contains $num_rows rows."
    exit 1

# Validate the data in the SQLite database
for row in profit_loss_data:
    year, quarter, profit_loss = row

    # Check that the year is an integer
    if not isinstance(year, int):
        echo "Error: The 'year' column should be an integer, but the value is \"$year\""
        exit 1

    # Check that the quarter is an integer
    if not isinstance(quarter, int):
        echo "Error: The 'quarter' column should be an integer, but the value is \"$quarter\""
        exit 1

    # Check that the profit_loss is a float
    if not isinstance(profit_loss, float):
        echo "Error: The 'profit_loss' column should be a float, but the value is \"$profit_loss\""
        exit 1

# Execute the tests
python tests.py

# Display a success message
echo "Success: The data pipeline executed successfully and the output file \"data/FEU_profit_loss_data.db\" was created."
