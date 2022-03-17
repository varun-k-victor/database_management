import sqlite3

def connect():
    return sqlite3.connect("employees.db").cursor()

def field(connection):
    connection.execute("create table if not exists info(id integer primary key,name text,age integer)")
    
def input_name():
    return input("enter name:")

def input_age():
    return int(input("enter age:"))
   
def value(connection):
    name=input_name()
    age=input_age()
    connection.execute("insert into info(name,age) values(?,?)",(name,age))
    
def retrieve(connection):
    iid=int(input("enter id:"))
    connection.execute("select * from info where id=?",(iid,))
    print(connection.fetchall())
    
def delete(connection):
    iid=int(input("enter id:"))
    connection.execute("delete from info where id=?",(iid,))