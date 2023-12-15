FROM python:3.11

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app
RUN chmod +x start.sh
ENV TZ Europe/Moscow

ENV PYTHONUNBUFFERED=1
