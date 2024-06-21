#!/bin/sh

while ! pg_isready -q -h localhost -p $DB_PORT -U $DB_USER; do
  echo "Waiting PostgreSQL start"
  sleep 1
done

while [ "$(ls -1 $DB_BACKUP_PATH | wc -l)" -ge 5 ]; do
  OLDEST_BACKUP=$(ls -1t $DB_BACKUP_PATH | tail -n 1)
  rm "$DB_BACKUP_PATH/$OLDEST_BACKUP"
done

pg_dump -U $DB_USER -d $DB_NAME > "$DB_BACKUP_PATH/backup$(date + '%Y-%m-%d_%H-%M-%S').sql"
