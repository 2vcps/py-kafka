import sys
import os
import platform
import json
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
    order_id = randint(10000, 999999999)
    data = {
	"OrderId": order_id,
	"Email": "jo@portworx.com",
	"Main": "Smoked Brisket",
	"Side1": "Cornbread",
	"Side2": "Corn Pudding",
	"Drink": "Unsweet Tea",
	"Restaurant": "PXBBQ",
	"Date": "20 March 2023",
	"Street1": "1234",
	"Street2": "",
	"City": "ae3ei",
	"State": "GA",
	"Zip": "30158",
	"OrderStatus": "Pending"
    }
    #d = json.dumps(data)
    #data = {'counter': j}
    producer.send("order", data)
    #print(d)
    sleep(0.1)

