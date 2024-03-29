## Implemented APIs

### User sign up

  API for user sign up
   

  Curl:
  ```
  curl --location 'http://127.0.0.1:5000/signup' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "username": "sangamesh",
      "email": "sangameshkulkarni26@gmail.com",
      "password": "password"
  }'
  ```
  
Cases covered:
* User sign up
* Error out for already existing user sign up

### User login

Api for user login

```
curl --location 'http://127.0.0.1:5000/login' \
--header 'Content-Type: application/json' \
--data '{
    "username": "sangamesh",
    "password": "password"
}'
```

Cases covered:
* Login of user with valid and invalid creds

### CSV upload

* API for csv upload

curl:

```
curl --location 'http://127.0.0.1:5000/upload_csv' \
--form 'file=@"path"'
```

Cases covered:
* Implemented like background task
* Whenever csv upload request comes in, response out the message and task_id and upload the csv in background
* Have used celery with redis as broker.


### Upload status

* API for csv upload status

curl:

```
curl --location 'http://127.0.0.1:5000/fetch_csv_status/b5b73d35-9969-4220-9593-f05963c8759b'
```

Cases covered:
* While uploading the csv, it is also implemented to update the status for that celery task
* With the given task id, fetch the status
* At the beginning, the status is marked as `Pending`
* When record gets added in db, the status is changed to `Progress`
* Then when completes, the status is `Success`

  
### Get content

* API for the available imdb contents to show with pagination

curl:

```
curl --location 'http://127.0.0.1:5000/get_content?limit=5&offset=2'
```

Cases covered:
* Default limit is taken as 20 and offset as 1 if not given
* Supports pagination


### Requirements:

Flask
Celery (For async csv upload)
redis (I am on windows, redis is not officially supported. I have installed in wsl and ported it to windows)
mongodb

### How to run

Run `python run.py` to start the server
Run `celery -A application.workers.upload_csv_worker  worker --pool=solo -l info` to start executing the async tasks
