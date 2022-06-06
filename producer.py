import sys
import os
import platform
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

for j in range(9999):
    print("Iteration", j)
    # print(server_value)
    # print(user_value)
    # print(password_value)
    data = {'counter': j}
    producer.send(kf_topic, {key_value: data})
    sleep(0.05)

