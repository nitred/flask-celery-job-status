"""Create a global instance of celery with global config params."""
from flask_celery_job_status.server import create_celery_app

celery = create_celery_app()
