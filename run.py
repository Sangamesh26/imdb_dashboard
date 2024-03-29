from application import app

if __name__ == "__main__":
    app.run(debug=True)
    

# Installed celery for async csv file upload
#    Command followed is pip install celery
# Install redis, I have installed redis in wsl2-ubuntu using SNAP 
#    Command followed is sudo snap install redis
# pip install eventlet (celery task run)
# celery -A my_project_name worker --pool=solo -l info (single threaded)