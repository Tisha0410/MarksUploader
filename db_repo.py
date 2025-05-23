# Functions to interact with the database
from app.db import get_db
import psycopg2
import logging


def insert_db(student_details):
    try:
        conn = get_db()
        cur = conn.cursor()
        query = """ INSERT INTO student_marks (sid, english, math, physics, chem, bio, total, percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
        cur.executemany(query,student_details)
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        logging.error(("Database insertion error: %s", e ) + "line number:"+str(e.__traceback__.tb_lineno))
        return False
    finally:
        if conn:
            conn.close()
            print("DB connection closed.")




