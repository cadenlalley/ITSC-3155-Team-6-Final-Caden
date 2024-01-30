FROM tiangolo/uwsgi-nginx:python3.10

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn


COPY . .

CMD ["gunicorn", "--conf", "/app/petpals/gunicorn_conf.py", "--worker-class", "eventlet", "--bind", "0.0.0.0:80", "petpals:app"]

