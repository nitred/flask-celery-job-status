"""Flask Celery Job Status Server."""
import logging

from flask import Flask
from flask_celery_job_status.blueprints.factory_task_status import \
    factory_task_status_handler
from flask_celery_job_status.blueprints.job_status import job_status_handler
from flask_celery_job_status.blueprints.landing import landing_handler
from flask_celery_job_status.blueprints.naive_task_status import \
    naive_task_status_handler

logger = logging.getLogger(__name__)


def register_app(app):
    """Initialize blueprints."""
    app.register_blueprint(landing_handler, url_prefix="/", )
    app.register_blueprint(naive_task_status_handler, url_prefix="/naive_task_status", )
    app.register_blueprint(factory_task_status_handler, url_prefix="/factory_task_status", )
    app.register_blueprint(job_status_handler, url_prefix="/job_status", )


def create_app():
    """Configure the app w.r.t. Flask security, databases, loggers."""
    app = Flask(__name__,
                instance_relative_config=True,
                static_folder='static',
                static_url_path='/static')
    register_app(app)
    return app
