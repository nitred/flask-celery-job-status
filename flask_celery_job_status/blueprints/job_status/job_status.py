"""Job Status Blueprint."""
import logging
import os
import uuid

from flask import (Blueprint, current_app, jsonify, render_template, request,
                   url_for)

logger = logging.getLogger(__name__)

job_status_handler = Blueprint(name='job_status',
                               import_name=__name__,
                               template_folder='templates',
                               static_folder='static')


@job_status_handler.route('/', methods=['GET'])
def index():
    """Job Status Index."""
    return render_template('job_status_index.html')


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
