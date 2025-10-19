import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user ="shem",password = "1234")

mycursor = mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
    print(i)