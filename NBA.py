import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error
players= pd.read_csv("C:/Users/Suraj Parui/Desktop/NBA/Players.csv")
players=players.fillna("0")
try:
    conn = mysql.connect(host='localhost', database='nba', user='root', password='Sj@19691201')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record[0])
        cursor.execute('DROP TABLE IF EXISTS nba.players;')
        print('Creating table....')
        cursor.execute("CREATE TABLE nba.players(name varchar(255),height int,weight int,college varchar(255),bornyear int,birthcity varchar(255),birthstate varchar(255))")
        print("Table is created....")
        for i,row in players.iterrows():
            sql = "INSERT INTO nba.players VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)