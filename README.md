# Simple Flask app to send email asynchronously and get token

I use **Celery** to handle email asynchronously.

## How to run

1. `export MAIL_USER=your_email@gmail.com`: This email will be the sender
2. `export MAIL_PASSWORD=your_password`
3. Navigate to *web* --> *thea_web* --> *app.py*, line 46; change recipients email
4. `docker-compose build`
5. `docker-compose up`

## Folder

1. **docker**: contain database to store user and token
2. **nginx**
3. **thea_web**: contain Celery, Flask, Flask-Mail, gunicorn, and redis
4. Feel free to modify any file.

## Route inside app:

1. http://localhost: Expected output: Hello World!
2. http://localhost/download?token=123: Expected output: Bad token
3. http://localhost/download?token=12345: Expected output: Good token. There is also an email send to recipients email


## Resources and links:
1. [http://www.celeryproject.org](http://www.celeryproject.org/)
2. [https://blog.miguelgrinberg.com/post/using-celery-with-flask](https://blog.miguelgrinberg.com/post/using-celery-with-flask)
3. [https://pythonhosted.org/Flask-Mail](https://pythonhosted.org/Flask-Mail)