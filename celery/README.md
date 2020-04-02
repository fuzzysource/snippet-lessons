# Celery

## Scenario

I want to separate the code base of worker from the code base of
celery app so that development of the two services is
independent. This usage can be extended futher by writing celery
application or celery worker in languages rather than Python.

## Resolution

Use Celery's `signature` method to compose external task.

## Usage

```shell
# start redis container

docker-compose up -d

# Install dependencies

poetry install

# In a terminal, start the worker

poetry shell                        # activate the virtualenv
celery -A worker worker

# In other terminal, start the application

poetry shell                        # activate the virtualenv
python server.py

```
