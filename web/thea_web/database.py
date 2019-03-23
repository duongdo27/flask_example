import pymysql
from pymysql.cursors import DictCursor
from contextlib import contextmanager


@contextmanager
def connect():
    conn = pymysql.connect(
        host='db',
        user='root',
        password='root',
        database='thea',
        cursorclass=DictCursor,
    )
    cursor = conn.cursor()
    yield conn, cursor
    conn.close()


def query_data(query):
    with connect() as (conn, cursor):
        cursor.execute(query)
        result = cursor.fetchall()
    return result
