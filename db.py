import psycopg2
from flask import g 
import os
import logging

logging.basicConfig(level=logging.ERROR)
#function to connect to the database
def get_db():
    try:
        if 'db' not in g or g.db.closed:
            g.db  = psycopg2.connect(
                host= "hostname",
                port="port_name",
                database="db_name",
                user="username",
                password="*****"
            )
        print("DB connection established.")
        return g.db
    except Exception as e:
        logging.error(("Unable to connect to database: %s", e ) + "line number:"+str(e.__traceback__.tb_lineno))
        return None

#function to close the database connection
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        print("DB connection closed.")
    else:
        print("No DB connection found.")

#function to create the database
    

    

