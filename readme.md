# Data Processing

This repository contains two Python scripts for processing data:

1. `data.py`: This script reads data from a JSON file and prints the population of Ghana, the number of active cases, the number of recovered cases, the number of deaths, and the number of tests conducted in Ghana. It also prints the population of Ghana as a separate variable.

2. `load_data_into_mysql.py`: This script loads the data from the JSON file into a MySQL database. It creates a table in the database and inserts the data into the table.

## Usage

To use the scripts, follow these steps:

1. Install the required packages:mysql-connector-python

2. Run the `data.py` script

3. Run the `load_data_into_mysql.py` script

Note: Make sure to replace the placeholders in the scripts with the actual values for your MySQL database.

## Requirements

- Python 3.x
- mysql-connector-python package

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
