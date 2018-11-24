import psycopg2


def get_connection():
    db = psycopg2.connect(dbname="news")
    return db.cursor()
