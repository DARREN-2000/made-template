#!/bin/bash

# Install the required Python libraries
pip install pandas requests sqlite3

# Stop on first error
set -o errexit

# Create a directory for temporary files
mkdir -p /tmp/tests

# Define the data pipeline script
data_pipeline_script=data_pipeline.py

# Execute the data pipeline script
python $data_pipeline_script 

# Execute the data pipeline
python pipeline.py /tmp/tests

# Validate that the output file exists
if [[ ! -f data/merged_data.csv ]]; then
  echo "Failed: Output file 'merged_data.csv' does not exist"
  exit 1
fi

# Validate that the output file exists
if [[ ! -f data/merged_data.db ]]; then
  echo "Failed: Output file 'merged_data.db' does not exist"
  exit 1
fi

# Execute the tests
python tests.py

# Remove the temporary directory
rm -rf /tmp/tests

echo "All tests passed"
