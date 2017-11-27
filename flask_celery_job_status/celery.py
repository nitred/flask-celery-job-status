"""Create a global instance of celery with global config params."""
from celery import Celery

celery = Celery(__name__,
                backend='redis://localhost:6379',
                broker='redis://localhost:6379')
