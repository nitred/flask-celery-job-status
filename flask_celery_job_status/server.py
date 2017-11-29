"""Flask Celery Job Status Server."""
import logging

from celery import Celery
from flask import Flask

logger = logging.getLogger(__name__)


def create_naive_app():
    """Plain app."""
    app = Flask(__name__,
                static_folder='static',
                static_url_path='/static')
    return app


def create_celery_app(app=None):
    """Create celery instance with flask app context.

    Source: https://gist.github.com/anonymous/fa47834db2f4f3b8b257
    Source: https://stackoverflow.com/questions/25360136/flask-with-create-app-sqlalchemy-and-celery
    """
    app = app or create_naive_app()
    celery = Celery(__name__,
                    backend='redis://localhost:6379',
                    broker='redis://localhost:6379',
                    include=[
                        'flask_celery_job_status.blueprints.naive_task_status.tasks',
                        'flask_celery_job_status.blueprints.factory_task_status.tasks',
                        'flask_celery_job_status.blueprints.job_status.tasks'
                    ])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    celery.app = app
    return celery


def register_app(app):
    """Initialize blueprints."""
    from flask_celery_job_status.blueprints.factory_task_status import \
        factory_task_status_handler
    from flask_celery_job_status.blueprints.job_status import job_status_handler
    from flask_celery_job_status.blueprints.landing import landing_handler
    from flask_celery_job_status.blueprints.naive_task_status import \
        naive_task_status_handler

    app.register_blueprint(landing_handler, url_prefix="/", )
    app.register_blueprint(naive_task_status_handler, url_prefix="/naive_task_status", )
    app.register_blueprint(factory_task_status_handler, url_prefix="/factory_task_status", )
    app.register_blueprint(job_status_handler, url_prefix="/job_status", )


def create_app():
    """Configure the app w.r.t. Flask security, databases, loggers."""
    app = Flask(__name__,
                static_folder='static',
                static_url_path='/static')
    register_app(app)
    return app
