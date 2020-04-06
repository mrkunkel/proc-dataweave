FROM python:3.7-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./app.py ./
COPY ./dw /root/.dw/

RUN pip install Flask gunicorn requests

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
