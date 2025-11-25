import os
from typing import Union
import mysql.connector
import psycopg2

from logging import Logger
from dotenv import load_dotenv
from mysql.connector.connection_cext import CMySQLConnection

# load varaibles environment
load_dotenv()


def create_mysql_connection(logger: Logger) -> Union[CMySQLConnection, -1]:
    
    try:
        conn = mysql.connector.connect(
            user=os.environ["MYSQL_USER"],
			password=os.environ["MYSQL_PWD"],
			host=os.environ["MYSQL_HOST"],
			database=os.environ["MYSQL_DB"])
        
        logger.info("create_mysql_connection - staging datawarehouse: Connected")
        
        return conn
    
    except mysql.connector.OperationalError as e:
        logger.critical(f"create_mysql_connection - Connection failed : {e}")
        return -1
    
    except mysql.connector.Error as e:
        logger.critical(f"create_mysql_connection - unexpected error: {e}")
        return -1


def create_postgres_connection(logger: Logger):
    """Connect to the Postgres database"""
    
    try:
        conn = psycopg2.connect(
		database = os.environ["POSTGRES_DB"], 
		user = os.environ["POSTGRES_USER"],
		password = os.environ["POSTGRES_PWD"],
		host = os.environ["POSTGRES_HOST"], 
		port = os.environ["POSTGRES_PORT"])
        
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1;")
        
        logger.info("create_postgres_connection - production datawarehouse: Connected")
        return conn
    
    except psycopg2.OperationalError as e:
        logger.critical(f"create_postgres_connection - Connection failed: {e}")
        return -1


def insert_to_database(conn, sql_statement: str, logger: Logger):
  
	try:
		cursor = conn.cursor()
		cursor.execute(sql_statement)
		conn.commit()
	
	except Exception as e:
		logger.error(f"insert_to_database - unexpected error: {e}")
		os._exit(1)


def query_database(connection: CMySQLConnection, sql_statement: str, logger: Logger):
    """summary"""
    
    try:
        cursor = connection.cursor()
        cursor.execute(sql_statement)
        rows = cursor.fetchall()
        
        if len(rows) == 1:
            return rows[0]
        return rows
            
    except Exception as e:
        logger.error(f"query_database - unexpedted error: {e}")
        return -1
    
    finally:
        connection.close()



if __name__ == "__main__":
   pass
	