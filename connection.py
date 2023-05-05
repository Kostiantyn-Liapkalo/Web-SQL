
from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    """ create a database connection to a postgres database """
    connection = None
    try:
        connection = connect(host='balarama.db.elephantsql.com', user='vddxqzuw', password='Gg56Z6axtE7pVhSFlxRMP8ipVQRe9yes', database='vddxqzuw')
        yield connection
        connection.commit()
    except Error as err:
        print(err)
        connection.rollback()
    finally:
        if connection:
            connection.close()
