# syntax=docker/dockerfile:1
# Create Flask Container
FROM python:3.12.1-alpine3.18

WORKDIR /app

COPY /* /app
RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]


