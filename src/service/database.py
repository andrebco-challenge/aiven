import psycopg2


def create_connection():
    return psycopg2.connect(user="user", password="password", host="localhost", port="5432", database="database")


# Refactoring of Singleton or possible connection manager.
class Connection:
    class __Connection:
        def __init__(self):
            self.conn = create_connection()

    instance = None

    def __init__(self):
        if not Connection.instance:
            Connection.instance = Connection.__Connection()
        else:
            Connection.instance.conn = create_connection()


def connect():
    Connection()
    print('Connection to database succeeded...')
