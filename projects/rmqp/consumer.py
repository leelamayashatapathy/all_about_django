import pika
import pandas as pd
import json
import uuid


def generateExcel(message):
    message = json.loads(message)
    df = pd.DataFrame(message)
    df.to_excel(f'output{uuid.uuid4()}.xlsx', index=False)

def callback(ch, method, properties, body):
    message = body.decode()
    generateExcel(message)
    
    
params = pika.URLParameters('amqps://apkiaqzr:7c6TdpJsTwbenMlIt1IG5DFd5LnZrHbE@puffin.rmq2.cloudamqp.com/apkiaqzr')
connection = pika.BlockingConnection(params)
channels = connection.channel()
channels.queue_declare(queue="my_queue")
channels.basic_consume(queue='my_queue',on_message_callback=callback,auto_ack=True)
print("Consumerstarted")
channels.start_consuming()