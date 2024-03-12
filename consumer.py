import pika
import logging

logging.basicConfig(level=logging.INFO)


def callback(ch, method, properties, body):
    logging.info(f"Received message: {body}")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()

    channel.queue_declare(queue='golang-queue', durable=False, exclusive=False)

    channel.basic_consume(queue='golang-queue', on_message_callback=callback, auto_ack=True)

    logging.info("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == '__main__':
    main()
