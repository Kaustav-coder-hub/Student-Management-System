# models/student_model.pyimport sys

from utils.database_utils import get_connection


def add_student(first_name, middle_name, last_name, dob, email, major, year, phone, address, emergency):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO students (
            First_Name, Middle_Name, Last_Name, Date_of_Birth, Email, Major, 
            Year_of_Enrollment, Phone_Number, Address, Emergency_Contact_Number
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (first_name, middle_name, last_name, dob, email, major, year, phone, address, emergency)
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows
