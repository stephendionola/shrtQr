import os
import psycopg
from contextlib import contextmanager

@contextmanager
def get_connection():
    """Context manager for database connection."""
    print('Get connection called:')
    connection = psycopg.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", 5432)),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "password"),
        dbname=os.getenv("DB_NAME", "link_shortener"),
        row_factory=psycopg.rows.dict_row  # Ensures rows are returned as dictionaries
    )
    try:
        yield connection
    finally:
        connection.close()

def execute_query(query, params=None):
    """Execute a single query with optional parameters."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

def insert_one(query, params=None):
    """Fetch a single row from the database."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            res = cursor.fetchone()
            conn.commit()
            return res

def fetch_one(query, params=None):
    """Fetch a single row from the database."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()

def fetch_all(query, params=None):
    """Fetch all rows from the database."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

