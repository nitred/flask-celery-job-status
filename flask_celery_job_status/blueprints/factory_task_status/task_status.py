"""Job Status Blueprint."""
import logging
import random

from flask import Blueprint, current_app, redirect, render_template, url_for

from .tasks import add_two_numbers, celery

logger = logging.getLogger(__name__)

factory_task_status_handler = Blueprint(name='factory_task_status',
                                        import_name=__name__,
                                        template_folder='templates',
                                        static_folder='static')


def get_all_tasks():
    """Return list of all tasks."""
    return current_app.config['all_tasks']


def delete_all_tasks():
    """Empty the list of all tasks."""
    current_app.config['all_tasks'] = []


@factory_task_status_handler.before_app_first_request
def before_app_first_request():
    """Create some global resources before first request."""
    current_app.config['all_tasks'] = []


@factory_task_status_handler.route('/', methods=['GET'])
def index():
    """Job Status Index."""
    return render_template('fts_index.html')


@factory_task_status_handler.route('/create_task', methods=['GET'])
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
    return redirect(url_for('factory_task_status.task_status'))


@factory_task_status_handler.route('/task_status', methods=['GET'])
def task_status():
    """Show all task status."""
    all_tasks = get_all_tasks()
    return render_template('fts_task_status.html', tasks=all_tasks)


@factory_task_status_handler.route('/clear_tasks', methods=['GET'])
def clear_tasks():
    """Create a task."""
    # NOTE: Purging does not work!
    celery.control.purge()
    delete_all_tasks()

    # Redirecting to the task status.
    return redirect(url_for('factory_task_status.task_status'))
