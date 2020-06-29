import sqlite 3
from sqlite3 imprt Error
from csv import DictReader
import os




def GetOrCreateDBConn(db_file):
    conn=None
    if os.path.exists(db_file):
        print("Creating connection to {}".format(db_file))
    else:
        print("creating new sqlite3 db at {}".format(db_path))
    try:
        conn=sqlite3.connect(db_file)
        print("{} succesffully opened".format(db_file))
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn
        else:
            return None

def PopulateDB(conn,csv_path):
    with open(csv_path,"r") as f:
        data=csv.DictReader(f)
    if data:
        columns=list(data.keys()) 
    else:
        raise Exception("The csv file priovided could not be understood")
    table_name=os.path.splitext(csv_path)[0]
    c=conn.cursor()
    column_maker = ",".join(["{} TEXT".format(column) for column in columns])
    #make a table with all data arranged according to an index
    c.execute("CREATE TABLE master ([generated_id] INTEGER PRIMARY KEY,{})".format(column_maker))
    for row in data:
        values=[row.get(k) for k in columns]
        
    
    
    #make a seperate table for each column using its vlaue as the primary key, to speed up a search operation using a specific column such as performer
    for column in columns:
        tmp=columns
        primary_key=column
        other_columns=tmp.pop(primary_key)
