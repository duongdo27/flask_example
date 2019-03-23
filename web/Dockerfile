FROM python:3.6.1-slim

WORKDIR /code

COPY web/requirements.txt .
RUN pip install -r requirements.txt

COPY web .
RUN pip install -e .

ENTRYPOINT ["gunicorn"]
CMD ["--workers=4", "--bind=0.0.0.0:8000", "--log-level=info", "thea_web.app:app"]
