import logging
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    app.logger.info('Route hello visited')
    return 'Hello World!'


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
