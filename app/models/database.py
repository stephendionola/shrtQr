import pymysql
import os

def get_connection():
    print('Getting connection')
    con = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "link_shortener"),
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Got connection!\n Returning...')

    return con
