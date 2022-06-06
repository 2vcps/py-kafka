import sys
import os
from time import sleep
from json import dumps
from kafka import KafkaConsumer

server_value = str(os.getenv("KF_SERVER"))
user_value = str(os.getenv("KF_USERNAME"))
password_value = str(os.getenv("KF_PASSWORD"))
kf_topic = str(os.getenv("KF_TOPIC"))

consumer = KafkaConsumer(
    kf_topic,
    bootstrap_servers= server_value,
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username= user_value,
    sasl_plain_password= password_value
)

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

