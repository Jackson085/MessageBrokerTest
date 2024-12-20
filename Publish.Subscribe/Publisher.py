import pika

def publish_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Exchange erstellen
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    message = "Hello, this is a broadcast message!"
    channel.basic_publish(exchange='logs', routing_key='', body=message)

    print(f"Sent: {message}")
    connection.close()

if __name__ == '__main__':
    publish_message()
