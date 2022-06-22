from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as pl
from tkcalendar import *
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error
players= pd.read_csv("C:/Users/Suraj Parui/Desktop/NBA/Players.csv")
players=players.fillna("0")
players_data= pd.read_csv("C:/Users/Suraj Parui/Desktop/NBA/player_data.csv")
players_data=players_data.fillna("0")
season= pd.read_csv("C:/Users/Suraj Parui/Desktop/NBA/Seasons_Stats.csv")
season=season.fillna("0")
print(players,players_data,season)