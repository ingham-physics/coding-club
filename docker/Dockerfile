FROM ubuntu:20.04

RUN apt-get update; apt-get install -y python3 python3-pip git

RUN ln -s /usr/bin/python3 /usr/bin/python

COPY example/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY example/app.py /app.py

EXPOSE 8050

ENTRYPOINT  ["tail", "-f", "/dev/null"]
#CMD gunicorn app:server -b :$PORT
