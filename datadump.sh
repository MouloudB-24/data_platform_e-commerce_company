#!/usr/bin/bash

# stop on error
set -e

# Load configuration
source .env

# Export
echo "Start export table: $DB_TABLE"
mysqldump -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" --password="$DB_PASSWORD" "$DB_NAME" "$DB_TABLE" > "$EXPORT_DIR/${EXPORT_FILE}.sql"

