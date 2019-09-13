FROM postgres:11.2-alpine

#docker-entrypoint-initdb.d from the postgres image executes on init
#so add the create.sql file their
ADD create.sql /docker-entrypoint-initdb.d
