from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from datetime import datetime
def mock_table():
    query = """SELECT
               students.student_id,
               students.first_name,
               students.last_name,
               CASE
               WHEN attendance.student_id IS NOT NULL THEN 'Present' ELSE 'Absent'
               END as Attendance_Status
               FROM students
               Left JOIN attendance ON students.student_id = attendance.student_id AND attendance.a_date = '2021-04-20'"""
            

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        

        cursor = conn.cursor()
        cursor.execute(query)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
def main():
    
    mock_table()

if __name__ == '__main__':
    main()