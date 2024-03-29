from celery import Celery
from pymongo import MongoClient
from application import celery
import csv
from io import StringIO

client = MongoClient('mongodb://localhost:27017/')
db = client['imdb']

@celery.task(bind=True)
def process_csv(self, csv_data):
    csv_rows = csv_data.split('\n')
    title_row = csv_rows[0].split(',')
    
    csv_data_rows = csv_rows[1:]
    total_rows = len(csv_data_rows)
    current_row = 0
    
    self.update_state(state='PENDING',meta={'total_rows': total_rows,'current_row': current_row})
    
    for row in csv_data_rows:
        imdb_data = {}
        reader = csv.reader(StringIO(row))
        data_list = list(reader)[0]
        
        for idx,data in enumerate(title_row):
            imdb_data[data] = data_list[idx]
            
        db.uploads.insert_one({'data': imdb_data})
        current_row += 1
        # Updating the upload progress
        self.update_state(state='PROGRESS',
                          meta={'total_rows': total_rows,
                                'current_row': current_row})
    
    self.update_state(state='COMPLETE',meta={'total_rows': total_rows,'current_row': current_row})

    return {'total_rows': total_rows, 'current_row': current_row}
