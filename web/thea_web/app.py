import os
import logging
from time import sleep
from flask import Flask
from flask import request
from flask_mail import Mail
from flask_mail import Message
from celery import Celery
from thea_web.database import query_data

app = Flask(__name__)

# Celery config
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

celery = Celery(app.name,
                broker=app.config['CELERY_BROKER_URL'],
                backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)


# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)


@celery.task
def simple_task(x):
    print('Start simple task')
    sleep(x)
    print('Complete simple task')


@celery.task
def send_async_email():
    with app.app_context():
        msg = Message(subject='Hello from Flask',
                      body='Here is your information',
                      recipients=['dhdo@csbsju.edu'])
        mail.send(msg)


@app.route('/')
def index():
    app.logger.info('Route index visited')
    return 'Hello World!'


def get_token_lookup():
    query = """
        SELECT username, token
          FROM users
    """
    result = query_data(query)
    return {x['token']: x['username'] for x in result}


@app.route('/download')
def download():
    token = request.args.get('token')
    app.logger.info('token = %s', token)

    token_lookup = get_token_lookup()
    username = token_lookup.get(token)

    if username:
        app.logger.info('user = %s', username)
        simple_task.delay(10)
        send_async_email.delay()
        return 'Good Token!'
    else:
        return 'Bad Token!'


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
