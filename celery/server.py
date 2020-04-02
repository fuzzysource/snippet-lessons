from celery import Celery, signature

app = Celery(
    __name__, broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)

add_2_number = signature("add_2_numbers")

result = add_2_number.delay(3, 4)
r = result.get()
print("Result", r)
