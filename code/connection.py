import psycopg2

class Connection:

    def conn_local():
        conn = psycopg2.connect(
            host='postgres', 
            port='5432',
            database='postgres', 
            user='postgres',
            password='changeme'
            )

        return conn