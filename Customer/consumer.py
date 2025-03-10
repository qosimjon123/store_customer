import json
import logging
import threading
import pika
from .models import Client

RabbitUser = "user"
RabbitPassword = "password"
logging.basicConfig(level=logging.INFO)


def callback(ch, method, properties, body):
    data = json.loads(body)
    try:

        (customer, create) = Client.objects.get_or_create(user_id=data.get("user_id"))
        if create:
            logging.info(f"Created new customer with id :  {customer.user_id}")
        else:
            logging.info(f"Existing customer with id :  {customer.user_id}")

    except Exception as err:
        logging.error(f"Error processing message: {err}")

    return ch.basic_ack(delivery_tag=method.delivery_tag)



def consume_from_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbit-container',
        credentials=pika.PlainCredentials(RabbitUser, RabbitPassword),
    ))
    channel = connection.channel()
    channel.queue_declare(queue='customer-verified', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='customer-verified', on_message_callback=callback)
    logging.info('Consuming from RabbitMQ')
    channel.start_consuming()

def start_consumer():
    thread = threading.Thread(target=consume_from_rabbitmq, daemon=True)
    thread.start()