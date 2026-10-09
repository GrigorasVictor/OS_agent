FROM python:3.12-slim

WORKDIR /app
COPY src/ /app/src/
COPY requirements.txt /app/

RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["adk", "web"]

#FROM ubuntu:22.04
#
#RUN apt-get update
#RUN apt-get install -y python3
#RUN apt-get install -y python3-pip
#
#WORKDIR /app
#
#COPY src/ /app/src/
#COPY requirements.txt /app/
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#EXPOSE 8000
#
#CMD ["adk", "web"]
