from application.workers.upload_csv_worker import process_csv
from flask import jsonify

def upload_movies_csv(request):
    csv_file = request.files['file']
    
    # Start background task to process CSV
    task = process_csv.delay(csv_file.read().decode('utf-8'))
    
    return jsonify({'message': 'CSV upload processing started',
                    'task_id': task.id}), 202