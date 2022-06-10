from platform import python_version
from mysql.connector import connection
# import pandas as pd
print(python_version())


host = '192.168.104.6'
database = 'test_result'
user = 'neewee_root'
pass1 = 'neewee'
table_name = 'in4db'

conn = connection.MySQLConnection(user = user, host = host, passwd= pass1, database = database, charset="utf8mb4")
print("connection established...")
#my_data = pd.read_sql("SELECT * FROM test_result.in4db",conn)
#print(my_data)
#conn.close()

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM in4db")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)