import psycopg2
from config import DATABASE_CONFIG


def get_db_connection():
    return psycopg2.connect(**DATABASE_CONFIG)
