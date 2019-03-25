import os
import logging, threading, queue, time
from time import sleep
from flask import Flask
from flask import request
from flask_mail import Mail
from flask_mail import Message
from thea_web.database import query_data
from thea_web.ThreadSub import sleepsub


app = Flask(__name__)

# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'duongdopython@gmail.com'
app.config['MAIL_PASSWORD'] = 'Flask123'
app.config['MAIL_DEFAULT_SENDER'] = 'duongdopython@gmail.com'

mail = Mail(app)


@app.route('/')
def index():
    app.logger.info('Route index visited')
    return 'Hello World!'


@app.route('/thread')
def thread():
    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-10s) %(message)s',
                        )

    q = queue.Queue()

    s = '5'
    t = threading.Thread(name='Thread Test', target=sleepsub, args=(s, q))
    t.start()

    logging.debug("I can keep going.")

    while True:
        if t.isAlive():
            logging.debug("Is still active.")
            time.sleep(.5)
        else:
            logging.debug("Is no longer active.")
            return_value = q.get()
            logging.debug(return_value)
            break

    logging.debug("Let's continue.")
    return return_value


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
