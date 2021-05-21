from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from datetime import datetime

def insert_quary(name):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        dateTimeObj = datetime.now()
        dateObj = dateTimeObj.date()
        timeObj = dateTimeObj.time()
        
        data=(name,dateTimeObj)
        insert_sent=("INSERT INTO `attendance` (`student_id`,`a_timestamp`) VALUES (%s, %s)")
        cursor.execute(insert_sent, data)
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    name='8683257'
    insert_quary(name);