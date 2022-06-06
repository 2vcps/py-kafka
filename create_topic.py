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

topic = KafkaAdminClient(
    bootstrap_servers= server_value,
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username= user_value,
    sasl_plain_password= password_value
)

topic_list = []
topic_list.append(NewTopic(name=kf_topic, num_partitions=1, replication_factor=2))
topic.create_topics(new_topics=topic_list)



