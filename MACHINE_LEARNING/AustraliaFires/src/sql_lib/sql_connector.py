import pymysql as sq
import pymysql.cursors
import pandas as pd


def connector():
    conn = pymysql.connect(host='34.229.137.164',
                                user='student',
                                password='lebowsky',
                                database='australia_fires_2',
                                port=25001,
                                cursorclass=pymysql.cursors.DictCursor)
    return conn



def table_show():
    """Shows al table names from a database"""
    conn = connector()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES") 
    return cursor.fetchall()

def table_extractor(table):
    """Extracts a table from database to convert into DataFrame"""       
    query = f"""SELECT * FROM {table}"""
    conn = connector()
    return pd.read_sql_query(query, conn)
    