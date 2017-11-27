"""Tasks that need to be executed asynchronously."""
import random
import time

from flask_celery_job_status.celery import celery


@celery.task
def add_two_numbers(a, b):
    """A basic task that sleeps for some random time before returning sum."""
    time.sleep(random.randint(10, 100))
    return a + b
