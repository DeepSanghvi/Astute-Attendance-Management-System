from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from datetime import datetime
def insert_data(name,date,time):
    query = "INSERT INTO attendance(student_id,a_date,a_timestamp) " \
            "VALUES(%s,%s,%s)"
    correction ="select distinct student_id,a_date from attendance"
    args = (name,date,time)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        

        cursor = conn.cursor()
        cursor.execute(query, args)

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