import mysql.connector
import sys

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="students_manager"
)
db_cursor = db.cursor()


def get_students(): 
  db_cursor.execute("SELECT * from students")
  result = db_cursor.fetchall()
  return result

def add_student(name,mark):
  #Potential SQLi [security test]
  #Use prepared statement
  query = "INSERT INTO employees (name, mark) VALUES (%s, %s)"
  data = (name,mark)
  db_cursor.execute(query, data)
  result = db_cursor.fetchall()
  return result
def delete_student(id):
  query = "DELETE FROM students where id = %int"
  result = db_cursor.execute(query)
  return result

sys.modules["db_cursor"] = db_cursor
