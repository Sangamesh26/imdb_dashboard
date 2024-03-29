from flask import Flask
from celery import Celery

app = Flask(__name__)


# Update settings to use the new format
app.config['CELERY_TASK_INCLUDE'] = ['tasks']

# Set up Celery instance
celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

# Update Celery configuration
celery.conf.update(app.config)

from application import routes