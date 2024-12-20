import pika

def consume_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Exchange deklarieren
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    # Temporäre Queue erstellen
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Queue an den Exchange binden
    channel.queue_bind(exchange='logs', queue=queue_name)

    print("Waiting for messages. To exit press CTRL+C")

    def callback(ch, method, properties, body):
        print(f"Received: {body.decode()}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consume_message()
