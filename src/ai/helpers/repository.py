from service.database import Connection

# TODO: Use a proper library to create queries instead of raw sqls.
SELECT_STATUS_REQUEST_SUCCEEDED = "SELECT * FROM status_request_succeeded;"
SELECT_STATUS_REQUEST_FAILED = "SELECT * FROM status_request_failed;"
INSERT_STATUS_REQUEST_SUCCEEDED = (
    "INSERT INTO "
    "status_request_succeeded(timestamp, link, return_code, return_time, content_match) "
    "VALUES('{}', '{}', {}, {}, {}) RETURNING id;"
)
INSERT_STATUS_REQUEST_FAILED = (
    "INSERT INTO "
    "status_request_failed(timestamp, link, return_code, return_time) "
    "VALUES('{}', '{}', {}, {}) RETURNING id;"
)
DELETE_STATUS_REQUEST_SUCCEEDED = "DELETE FROM status_request_succeeded;"
DELETE_STATUS_REQUEST_FAILED = "DELETE FROM status_request_failed;"


def execute_query(query):
    try:
        conn = Connection().instance.conn
        with conn.cursor() as curs:
            curs.execute(query)
            conn.commit()
    except Exception as e:
        print("Failed query: {}".format(e))


def fetch_query(query):
    try:
        conn = Connection().instance.conn
        with conn.cursor() as curs:
            curs.execute(query)
            return curs.fetchone()
    except Exception as e:
        print("Failed query: {}".format(e))


def insert_status_request_succeeded(timestamp, link, return_code, return_time, content_match):
    query = INSERT_STATUS_REQUEST_SUCCEEDED.format(timestamp, link, return_code, return_time, content_match)
    execute_query(query)


def insert_status_request_failed(timestamp, link, return_code, return_time):

    query = INSERT_STATUS_REQUEST_FAILED.format(timestamp, link, return_code, return_time)
    execute_query(query)


def fetch_status_request_succeeded():
    return fetch_query(SELECT_STATUS_REQUEST_SUCCEEDED)


def fetch_status_request_failed():
    return fetch_query(SELECT_STATUS_REQUEST_FAILED)


def delete_status_request_succeeded():
    return execute_query(DELETE_STATUS_REQUEST_SUCCEEDED)


def delete_status_request_failed():
    return execute_query(DELETE_STATUS_REQUEST_FAILED)
