import pika
import time


#it uses AMQP to communicate 
credentials = pika.PlainCredentials('sabarish', 'Password123')
parameters = pika.ConnectionParameters('rabbitmq.selfmade.ninja', 5672, 'Sabarish_hello_world', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='hello',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()