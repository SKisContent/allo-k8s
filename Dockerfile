FROM python:3.11


WORKDIR /app
COPY ./allo /app/allo
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./uwsgi.ini /app/uwsgi.ini
CMD ["gunicorn", "--conf", "allo/gunicorn_conf.py", "--bind", "0.0.0.0:80", "allo.main:app"]
