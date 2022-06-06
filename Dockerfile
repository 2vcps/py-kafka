FROM python:latest

# COPY bots/config.py /bots/
# COPY bots/favretweet.py /bots/
# COPY bots/autoreply.py /bots/
# COPY bots/followFollowers.py /bots/
COPY producer.py /
COPY consumer.py /
COPY create_topic.py /
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /
CMD ["sleep", "84600"]