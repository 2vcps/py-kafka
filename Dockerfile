FROM python:latest

COPY producer.py /
COPY consumer.py /
COPY create_topic.py /
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /
CMD ["sleep", "84600"]