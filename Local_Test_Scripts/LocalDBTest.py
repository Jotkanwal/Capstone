import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="asdf123",
  database="capstone"
)

mycursor = mydb.cursor(buffered = True)
  
mycursor.execute("SELECT * FROM heuristics")
for x in mycursor:
  print(x)