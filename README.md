# NBA Data Analytics

This Python script performs data analytics on NBA player data and imports it into a MySQL database. It utilizes the `pandas` library to read data from a CSV file and the `mysql.connector` library to connect to the MySQL database.

## Prerequisites

Before running the script, ensure that you have the following installed:

- Python 3.x
- pandas library (`pip install pandas`)
- mysql-connector-python library (`pip install mysql-connector-python`)

## Instructions

1. Prepare the Data:
   - Place the `Players.csv` file in the desired location on your machine. Ensure that the file contains the necessary NBA player data.
   - Update the file path in the script to match the location of the `Players.csv` file:
     ```python
     players = pd.read_csv("C:/Users/Suraj Parui/Desktop/NBA/Players.csv")
     ```

2. Set up the MySQL Database:
   - Make sure you have MySQL installed and running on your machine.
   - Update the database connection details in the script:
     ```python
     conn = mysql.connect(host='localhost', database='nba', user='root', password='Sj@19691201')
     ```

3. Run the Script:
   - Execute the script by running the following command in the terminal or command prompt:
     ```bash
     python nba_data_analytics.py
     ```
   - The script will connect to the MySQL database and create a table named `players` in the `nba` database.
   - It will then insert the NBA player data from the CSV file into the `players` table.

4. Verify the Results:
   - Once the script finishes executing, you can check the MySQL database to ensure that the table and data have been imported successfully.

## Acknowledgements

The NBA Data Analytics script was developed to perform data analytics on NBA player data and import it into a MySQL database.
