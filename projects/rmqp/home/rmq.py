import pika
import json

def publish_message(message):
    params = pika.URLParameters('amqps://apkiaqzr:7c6TdpJsTwbenMlIt1IG5DFd5LnZrHbE@puffin.rmq2.cloudamqp.com/apkiaqzr')
    connection = pika.BlockingConnection(params)
    channels = connection.channel()
    channels.queue_declare(queue="my_queue")
    message = json.dumps(message)
    channels.basic_publish(
        exchange='',
        routing_key='my_queue',
        body=message
    )
    print(f"Message publishes {message}")
    connection.close()