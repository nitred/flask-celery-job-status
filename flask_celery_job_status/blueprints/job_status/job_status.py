"""Job Status Blueprint."""
import logging
import random

from flask import (Blueprint, current_app, jsonify, redirect, render_template,
                   request, url_for)

from .tasks import add_two_numbers, celery

# from flask_celery_job_status.celery import celery


logger = logging.getLogger(__name__)

job_status_handler = Blueprint(name='job_status',
                               import_name=__name__,
                               template_folder='templates',
                               static_folder='static')


def get_all_tasks():
    """Return list of all tasks."""
    return current_app.config['all_tasks']


def delete_all_tasks():
    """Empty the list of all tasks."""
    current_app.config['all_tasks'] = []


@job_status_handler.before_app_first_request
def before_app_first_request():
    """Create some global resources before first request."""
    current_app.config['all_tasks'] = []


@job_status_handler.route('/', methods=['GET'])
def index():
    """Job Status Index."""
    return render_template('job_status_index.html')


@job_status_handler.route('/create_task', methods=['GET'])
def create_task():
    """Create a task."""
    # Generating random argument values
    a, b = random.randint(0, 10), random.randint(0, 10)
    task = add_two_numbers.apply_async(args=[a, b])

    # Creating a custom task representation attribute in order to render it on the HTML
    task.task_repr = "{}({}, {})".format(add_two_numbers.__name__, a, b)

    # Adding the task to a global tasks list.
    # WARNING!!! This is BAD practice. Use a database instead.
    all_tasks = get_all_tasks()
    all_tasks.append(task)

    # Redirecting to the task status.
    return redirect(url_for('job_status.task_status'))


@job_status_handler.route('/task_status', methods=['GET'])
def task_status():
    """Show all task status."""
    all_tasks = get_all_tasks()
    return render_template('task_status.html', tasks=all_tasks)


@job_status_handler.route('/clear_tasks', methods=['GET'])
def clear_tasks():
    """Create a task."""
    # NOTE: Purging does not work!
    celery.control.purge()
    delete_all_tasks()

    # Redirecting to the task status.
    return redirect(url_for('job_status.task_status'))


@job_status_handler.route('/create_job', methods=['GET'])
def create_job():
    """Create Job."""
    ret_dict = {
        'good_job': url_for('job_status.index')
    }
    return jsonify(ret_dict)


@job_status_handler.route('/active_job_ids', methods=['GET'])
def active_job_ids():
    """Running Job IDs."""
    ret_dict = {
        'good_job': url_for('job_status.index')
    }
    return jsonify(ret_dict)


@job_status_handler.route('/job_id_status', methods=['GET', 'POST'])
def job_id_status():
    """Job ID Status."""
    ret_dict = {
        'job_id': request.args['job_id']
    }
    return jsonify(ret_dict)
