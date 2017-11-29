"""Create a global instance of celery with global config params."""
from celery import Celery

celery = Celery('tasks',
                backend='redis://localhost:6379',
                broker='redis://localhost:6379',
                include=[
                    'flask_celery_job_status.blueprints.naive_task_status.tasks',
                    'flask_celery_job_status.blueprints.factory_task_status.tasks',
                    'flask_celery_job_status.blueprints.job_status.tasks',
                ])
