FROM tiangolo/uwsgi-nginx-flask:python3.9

WORKDIR /app
COPY ./allo /app/allo
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./uwsgi.ini /app/uwsgi.ini
