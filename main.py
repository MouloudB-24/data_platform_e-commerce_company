from ETL.automation import get_last_rowid, get_latest_records, insert_records
from utils.logger import logger



def main():
    
    logger_ = logger("/home/mouloud/Documents/projects/data_platform_e-commerce_company/logger.log")
    
    logger_.info("*** Synchronization between staging and production DataWarehouses ***")
    logger_.info("start...")
    
    # Find out the last rowid from PostgreSql data warehouse
    last_row_id = get_last_rowid(logger_)

    # List out all records in MySQL database with rowid greater than the one on the Data warehouse
    new_records = get_latest_records(last_row_id, logger_)
    
    # Insert the additional records from MySQL into PostgreSql data warehouse
    insert_records(new_records, logger_)


if __name__ == "__main__":
    main()