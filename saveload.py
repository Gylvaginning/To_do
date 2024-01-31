import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ll",
  password="foaw12bvco"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE tasks")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)