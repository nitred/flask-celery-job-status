"""Mocker Service."""
import logging
import os

from flask import Flask
from flask_celery_job_status.blueprints.job_status import job_status_handler
from flask_celery_job_status.blueprints.landing import landing_handler
from flask_celery_job_status.blueprints.naive_task_status import \
    naive_task_status_handler

logger = logging.getLogger(__name__)

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(THIS_FILE_PATH), "../../"))
CONFIG_PATH = os.path.abspath(os.path.join(BASE_PATH, "config/config.yaml"))


def register_app(app):
    """Initialize blueprints."""
    app.register_blueprint(landing_handler, url_prefix="/", )
    app.register_blueprint(naive_task_status_handler, url_prefix="/naive_task_status", )
    app.register_blueprint(job_status_handler, url_prefix="/job_status", )


def create_app():
    """Configure the app w.r.t. Flask security, databases, loggers."""
    app = Flask(__name__,
                instance_relative_config=True,
                static_folder='static',
                static_url_path='/static')
    register_app(app)
    return app
