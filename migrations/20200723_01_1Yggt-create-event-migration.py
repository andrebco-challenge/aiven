"""Create Event Migration"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """CREATE TABLE status_request_succeeded (
            id serial PRIMARY KEY,
            timestamp TIMESTAMP,
            link varchar(255) NOT NULL,
            return_code integer NOT NULL,
            return_time integer NOT NULL,
            content_match boolean
        )""",
        "DROP TABLE status_request_succeeded",
    ),
    step(
        """CREATE TABLE status_request_failed (
             id serial PRIMARY KEY,
             timestamp TIMESTAMP,
             link varchar(255) NOT NULL,
             return_code integer NOT NULL,
             return_time integer NOT NULL
         )""",
        "DROP TABLE status_request_failed",
    ),
]
