==
Aivens Project
==

This code is meant to be the scaffold of the solution proposed to the code challenge.

The code is based on (deployment libs):
 - Python 3.8
 - Poetry
 - Tox
 - Psycopg2
 - yoyo-migrations
 - confluent-kafka
 - requests

The library set was chosen to be the simplest possible in order to get result with the minimum library set possible.

Overview
--------

The initial idea on the implementation was done considering the bare minimum set up for Kafka. Since the idea was to implement
``` a system that monitors website availability over the
network, produces metrics about this and passes these events through an Aiven
Kafka instance into an Aiven PostgreSQL database```, the solution implemented consider the traditional backbones of any Kafka application: Consumers, Producers and Integrations.

The overall abstraction is that we will have a producer generating messages every X seconds on a topic `status_request_created`that will be consumed
as soon as available by a worker `url_checker`. This worker will then check the messages and split the result into other
two topics: `status_request_succeeded` and `status_request_failed`. As the name says, the first will be addressing the succeeded
requests with the desired metrics and the second on on urls that presented issues on retrieval. Then these two topics will be consumed
by workers to persist on the database.

Considerations
--------------

 Here follows a brain dump of the ideas here considered.

 - Just producers and consumers were used on this implementation.
 - Majority of tests were Integration tests based on a local Docker-compose run.
 - I understand that the topic names should be representing business processes and flow and on this case, `status_request` was assumed to be the process name.
 - Instead of using any CRON job or an application (that could be offline due to bugs), I opted for an application that would generate messages to the `url_checker` as well. This was done mainly because we could in the next steps use Kafka to store the next requests to be done, and in case of any outages of the main application (url_checker) the other workers would still be able to check the metrics.
 - Since the problem is not complex, no further configuration on Group Ids were done.
 - On the main function of the `url_checker` we are using a pattern to validate the url. This pattern could easily be added to messages or DB, if needed.
 - Due to the absence of ORM or any major Schema library, the repository pattern was used to at least organise the SQL queries. In next iteration, I would at least use a connection manager instead of pure `psycopg`.
 - In order to keep simplicity, the whole idea is to have all workers isolated on processes. That's why we will have to trigger the individually.

 Things that would be implemented on next iterations:

 - Connection Managers on Kafka and DB.
 - Schema Registry
 - If Regex is know before the arrival of the message, the compilation could be done on start time instead of execution time.
 - Increase test coverage currently on 38%. Add more unit tests.
 - Organisation of the code on DDD.
 - Adding a validation on the pattern regex.
 - DB indexes to be created according to usage. Business usage needed to be defined.
 - Links to be parsed would be stored on another system or on a table on the DB to give it more flexibility.
 - Use AsyncIo capabilities.
 - Major change on the processing of the `succeeded` and `failed` messages. I would use Faust to process them in a time windows so I would compact results and metrics saving DB queries and execution time. This would also allow us to have better visibility on results in case of outages. Time window would be of 5 minutes.
 - Integrate with Aivens DB and Kafka.

Execution
----------

Start `docker-compose` locally:

```
docker-compose up
```

Trigger migration controller Yoyo

```
make run migrate
```

Start Scheduler of Url Checker

```
poetry run task_scheduler
```

Start first worker `url_consumer`

```
poetry run url_consumer
```

Start persistence layer for Succeeded request

```
poetry run succeeded_consumer
```
Start persistence layer for Failed request

```
poetry run failed_consumer
```

For all the test tasks, please check Make file.

```
make test
make test-coverage
```

References
----------

Repository based on:

- https://github.com/audreyr/cookiecutter

Links used:

- https://pynative.com/python-postgresql-tutorial/
- https://github.com/confluentinc/confluent-kafka-python/tree/master/examples
