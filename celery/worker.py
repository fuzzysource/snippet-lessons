import time
from celery import Celery

app = Celery(
    __name__, broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@app.task(name="add_2_numbers")
def add(x, y):
    time.sleep(5)
    return x + y
