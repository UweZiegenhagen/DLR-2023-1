# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:17:11 2023

@author: Uwe
"""


import mysql.connector
import pandas as pd
from sqlalchemy import create_engine



"""
# example for the mysql connector package
mydb = mysql.connector.connect(
  host="sql608.your-server.de",
  user="uwezie_2_r",
  password="",
  database="northwind"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""

# sqlalchemy example
db_connection_str = 'mysql+mysqlconnector://uwezie_2_r:@sql608.your-server.de/northwind'
db_connection = create_engine(db_connection_str)

# pandas reads a dataframe from SQL
df = pd.read_sql('SELECT * FROM customers', con=db_connection)
# '_' requires math mode => replace them
df.columns = df.columns.str.replace("_", "-")

df.to_latex("table.tex")
