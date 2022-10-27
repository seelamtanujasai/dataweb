import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("car_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Mercedes')")
cursor.execute("insert into list (description) values ('BMW')")
cursor.execute("insert into list (description) values ('Toyoto')")
cursor.execute("insert into list (description) values ('volkswagon')")
cursor.execute("insert into list (description) values ('suzuki')")

connection.commit()
connection.close()

print("done.")