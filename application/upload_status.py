from flask import jsonify
from celery.result import AsyncResult
from application import celery


def upload_status(task_id):
    task = celery.AsyncResult(task_id)
    if task.state == 'PENDING':
        status = 'Upload pending'
        progress = 0
    elif task.state == 'SUCCESS':
        status = 'Upload completed successfully'
        progress = 100
    elif task.state == 'FAILURE':
        status = 'Upload failed'
        progress = 0
    else:
        status = 'Upload in progress'
        progress = task.info.get('current_row', 0) / task.info.get('total_rows', 1) * 100

    return jsonify({'status': status, 'progress': progress})