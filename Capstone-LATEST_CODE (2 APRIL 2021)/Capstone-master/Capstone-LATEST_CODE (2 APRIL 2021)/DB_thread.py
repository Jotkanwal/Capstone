from time import sleep
import mysql.connector
import threading
import temp_control.py


global val
val=[]
global temp
global time


def db_checker():

    global x
    x=True
    while x==True:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="Poiu0981!(",
          database="capstone"
        )

        cur = mydb.cursor(buffered = True)
        cur.execute("SELECT EXISTS (SELECT 1 FROM control);")
        val = cur.fetchone()
        val=list(val)

        if val[0]!=0:
            cur = mydb.cursor(buffered = True)
            cur.execute("Select * from control")
            val = cur.fetchone()
            val=list(val)
            temp = val[0]
            time = val[1]
            print ("temp = "+str(temp)+ " C")
            print ("time = "+str(time)+ " seconds")

            temp_control.temp_control(temp, time)
            cur.execute("truncate table control")
            x=False


db_checker()
