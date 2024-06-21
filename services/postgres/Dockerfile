FROM postgres:16

COPY initdb.sh /docker-entrypoint-initdb.d/

COPY database_backup.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/database_backup.sh

#RUN mkdir -p /var/backups/db_backups

#RUN echo "0 0 * * * /usr/local/bin/database_backup.sh" > /etc/crontabs/root
#CMD [ "sh", "-c", "crond -f & docker-entrypoint.sh postgres" ]
