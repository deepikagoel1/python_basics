import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Life@123"
)
print(mydb)
mycursor = mydb.cursor()
# mycursor.execute('''CREATE TABLE test.test_t1(
#     c1 int,
#     c2 varchar(100),
#     c3 float,
#     c4 BOOLEAN,
#     c5 int
# )''')
# mycursor.execute('''CREATE TABLE test.test2(
#     c1 int,
#     c2 varchar(100),
#     c3 float,
#     c4 BOOLEAN,
#     c5 int
# )''')
# mycursor.execute('''insert into test.test2 values(1,"deepika",3.5,True,8)''')
# mydb.commit() # if we are inserting the data into a table then we have to commit the db connection to make data available permanently.

mycursor.execute('''select * from test.test2''')

for i in mycursor.fetchall():
  print(i)

mydb.close()