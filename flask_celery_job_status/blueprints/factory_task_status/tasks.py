"""Tasks that need to be executed asynchronously."""
import random
import time

from flask_celery_job_status.server import create_celery_app

celery = create_celery_app()


@celery.task
def add_two_numbers(a, b):
    """A basic task that sleeps for some random time before returning sum."""
    time.sleep(random.randint(5, 25))
    return a + b
