import pandas as pd
import pymysql

# Establish connection
connection = pymysql.connect(
host = 'localhost',       
user = 'root',   
password = '654321',
database = 'StudentDB'
)
cursor = connection.cursor()

# get table data from sql
def get_table_from_mysql(table_name):
    query = f"select * from {table_name}"  
    table_data = pd.read_sql(query, connection)
    return table_data

table_data = get_table_from_mysql("student_info")
#print(table_data)


# List all tables in the database
def list_all_table():
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
list_all_table()

# List all column in tables in the database
def list_all_column_in_table():
    cursor.execute("describe student_info_1;")
    columns = cursor.fetchall()
    print("column name is :\n")
    for c in columns:
        print(c[0])
list_all_column_in_table()

# Backup
def backup(path):
    cursor.execute("""
        SELECT * FROM your_table
        INTO OUTFILE '/path/to/backup.sql'
    """)
def restore(path):    
    # Restore
    cursor.execute("""
        LOAD DATA INFILE '/path/to/backup.sql'
        INTO TABLE your_table;
    """)
    connection.commit()
