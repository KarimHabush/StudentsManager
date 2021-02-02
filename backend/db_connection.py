import mysql.connector
import sys

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="students_manager"
)
db_cursor = db.cursor()


def get_students(): 
  db_cursor.execute("SELECT * from students")
  result = db_cursor.fetchall()
  return result
def delete_student(id):
  query = ("DELETE FROM students WHERE id = %s")
  result = db_cursor.execute(query,(id))
  return result
def add_student(name,mark): 
  query = ("INSERT INTO students (name, mark) VALUES (%s, %s)")
  data = (name,mark)
  try:
    db_cursor.execute(query, data)
    db.commit()
    result = "L'étudiant est ajouté avec succès"
  except Exception:
    result = "L'étudiant n'est pas ajouté"
  finally:
    db_cursor.close()
  return result




sys.modules["db_cursor"] = db_cursor
