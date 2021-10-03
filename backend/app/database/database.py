import sqlite3
from sqlite3 import Error
import os
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_databases():
    #Create database if it doesn't exist + engine
    engine = create_engine('sqlite:///bills_management.db', echo=True)
    Base.metadata.create_all(engine)

    #Connect to database and fill it with default parameters
    return db_connection("bills_management.db")


def db_connection(abacus_db_path):
    """Connect to the db file corresponding to the path.
    If the file does not exist then the function create the file

    Args:
        chirpstack_credentials_db_path (string): Path to the database file
    """

    sql_create_bills_table = """ CREATE TABLE IF NOT EXISTS bills (
                                        id integer PRIMARY KEY,
                                        amount FLOAT NOT NULL,
                                        paymentDate DATE NOT NULL,
                                        description CHAR(1000) NOT NULL
                                    ); """

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        firstName CHAR(50) NOT NULL,
                                        lastName CHAR(50) NOT NULL,
                                        login CHAR(50) NOT NULL,
                                        password CHAR(50) NOT NULL
                                    ); """

    conn = None
    try:
        conn = sqlite3.connect(abacus_db_path)
        c = conn.cursor()
        _execute_query(conn, sql_create_bills_table)
        c.execute(''' SELECT count(id) FROM bills ''')

        rows = c.fetchall()
        print("Contenu de isFull", rows)

        return conn
    except Error as e:
        print(e)

def _execute_query(conn, sql_query):
    try:
        c = conn.cursor()
        c.execute(sql_query)
        #Make the table creation persistent in the db
        conn.commit()
    except Error as e:
        print(e)


def get_bills(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM bills")
    rows = cur.fetchall()
    return rows[0]
