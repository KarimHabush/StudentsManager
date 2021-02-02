import mysql.connector
import sys

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="students_manager"
)
db_cursor = db.cursor()

sys.modules["db_cursor"] = db_cursor
