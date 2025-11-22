# Import libraries required for connecting to mysql

# Import libraries required for connecting to DB2 or PostgreSql

# Connect to MySQL

# Connect to DB2 or PostgreSql

# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

import os
import mysql.connector
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_last_rowid():
	conn = psycopg2.connect(
		database = os.environ["dsn_database"], 
		user = os.environ["dsn_user"],
		password = os.environ["dsn_pwd"],
		host = os.environ["dsn_hostname"], 
		port = os.environ["dsn_port"]
	)
	
	cursor = conn.cursor()
	sql_statement = "SELECT rowid FROM sales_data ORDER BY rowid DESC LIMIT 1"
	cursor.execute(sql_statement)
	last_row = cursor.fetchone()

	conn.close()
	return last_row[0]

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
	conn = mysql.connector.connect(
		user='root',
		password=os.environ["DB_PASSWORD"],
		host=os.environ["DB_HOST"],
		database='sales'
    )
	
	cursor = conn.cursor()
	
	sql_statement = f"SELECT * FROM sales_data WHERE rowid > {rowid}"
	cursor.execute(sql_statement)
	records = cursor.fetchall()
	
	conn.close()
	return  records
 

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", new_records)

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.

def insert_records(records):
    
	if not records:
		print("No new recordings!")
		os._exit(1)

	conn = psycopg2.connect(
		database = os.environ["dsn_database"], 
		user = os.environ["dsn_user"],
		password = os.environ["dsn_pwd"],
		host = os.environ["dsn_hostname"], 
		port = os.environ["dsn_port"]
	)
	
	cursor = conn.cursor()
	
	for record in records:
		sql_statement = f"INSERT INTO sales_data(rowid, product_id, customer_id, quantity) VALUES {record}" 
		cursor.execute(sql_statement)
		conn.commit()
	conn.close()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse

# disconnect from DB2 or PostgreSql data warehouse 

# End of program