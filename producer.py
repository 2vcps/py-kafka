import sys
import os
import platform
from random import randint
from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

server_value = str(os.getenv("KF_SERVER"))
user_value = str(os.getenv("KF_USERNAME"))
password_value = str(os.getenv("KF_PASSWORD"))
kf_topic = str(os.getenv("KF_TOPIC"))
key_value = str(platform.node())

producer = KafkaProducer(
    bootstrap_servers= server_value,
    value_serializer=lambda m: dumps(m).encode('ascii'),
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username= user_value,
    sasl_plain_password= password_value
)
while True:
    j = randint(1, 99999999)
    print("Iteration", j)
    data = {'counter': j}
    producer.send(kf_topic, {key_value: data})
    sleep(0.05)

