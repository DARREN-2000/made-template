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
cur.execute('SELECT count(*) FROM profit_loss_data')
num_rows = cur.fetchone()[0]
if num_rows != 2:
    echo "Error: The SQLite database should contain 2 rows, but it contains $num_rows rows."
    exit 1

# Display a success message
echo "Success: The data pipeline executed successfully and the output file \"data/FEU_profit_loss_data.db\" was created."
