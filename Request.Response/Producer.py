import time

import pika


def on_request(ch, method, properties, body):
    print(f"Received request: {body.decode()}")

    # Antwort anpassen
    if body.decode() == "What time is it?":
        response = "It's muffin time!"
        time.sleep(2)
    else:
        response = f"Response to: {body.decode()}"

    # Antwort senden
    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Queue für Anfragen deklarieren
    channel.queue_declare(queue='Request')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='Request', on_message_callback=on_request)

    print("Waiting for requests. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    # start first
    main()
