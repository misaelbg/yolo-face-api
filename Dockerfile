FROM nvcr.io/nvidia/tensorflow:19.05-py3

ENV RABBITMQ_URL=amqp://guest:guest@172.17.0.2:5672

RUN apt-get update -y \
    && apt-get install -y libsm6 libxext6 libxrender1
    
RUN apt-get update -y \
    && apt-get install -y git cmake software-properties-common

WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["/docker-entrypoint.sh"]
