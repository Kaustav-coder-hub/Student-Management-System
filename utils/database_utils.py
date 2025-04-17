import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2004",  # Replace with your actual password
        database="college_students_db"
    )
