import mysql.connector

#establish the connection
conn = mysql.connector.connect(user='root', password='root', host='localhost')

#Create a cursor object using the cursor() method
cursor = conn.cursor()

#Create Database
cursor.execute("DROP database IF EXISTS students_manager;")
cursor.execute("CREATE database students_manager;")
cursor.execute("use students_manager;")

#Create Tables 
cursor.execute("CREATE TABLE students(id int unsigned not null auto_increment, name varchar(100) not null, mark double not null, primary key (id));")

cursor.execute("describe students;")
print(cursor.fetchall())


#Closing the connection
conn.close()
