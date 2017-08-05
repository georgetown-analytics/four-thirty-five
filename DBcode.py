import psycopg2
import psycopg2.extras
import sys
import csv
import pandas as pd

con= None

try:

    con=psycopg2.connect("dbname='mydb' user='adammorris'")
    cur = con.cursor()

    cur.execute("CREATE TABLE contacts (id INT PRIMARY KEY, name VARCHAR,email VARCHAR, phone_no INT)")
    COPY Contacts FROM {'abc_123.csv'}
    con.commit()

except psycopg2.DatabaseError as e:
    print (e)
    sys.exit(1)

finally:

    if con:
        con.close()
