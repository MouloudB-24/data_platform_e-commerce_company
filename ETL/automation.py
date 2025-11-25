# Import libraries required for connecting to mysql

# Import libraries required for connecting to DB2 or PostgreSql

# Connect to MySQL

# Connect to DB2 or PostgreSql

# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

import os
from typing import List
from dotenv import load_dotenv
from logging import Logger


from utils.db_connection import (
    create_mysql_connection,
    create_postgres_connection,
    insert_to_database,
    query_database,
)

# Load environment variables
load_dotenv()


def get_last_rowid(logger: Logger):
    """summary"""
    conn = create_postgres_connection(logger)
    if conn == -1:
        os._exit(1)

    sql_statement = "SELECT rowid FROM sales_data ORDER BY rowid DESC LIMIT 1"
    last_rowid = query_database(conn, sql_statement, logger)[0]
    if last_rowid == -1:
        os._exit(1)

    logger.info("Last row id on production datawarehouse")
    logger.info(last_rowid)

    return last_rowid


# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.


def get_latest_records(rowid: int, logger: Logger):
    conn = create_mysql_connection(logger)
    if conn == -1:
        os._exit(1)

    sql_statement = f"SELECT * FROM sales_data WHERE rowid > {rowid}"
    records = query_database(conn, sql_statement, logger)
    if not records:
        logger.info("No new recordings!")
        os._exit(1)

    logger.info("Number new rows on staging datawarehouse")
    logger.info(len(records))

    return records


# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.


def insert_records(records: List, logger: Logger):

    conn = create_postgres_connection(logger)

    for record in records:
        sql_statement = f"INSERT INTO sales_data(rowid, product_id, customer_id, quantity) VALUES {record}"
        insert_to_database(conn, sql_statement, logger)

    logger.info("Number new rows inserted into production datawarehouse")
    logger.info(len(records))

    conn.close()
