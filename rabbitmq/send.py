import pika
import sys


#it uses AMQP to communicate 
credentials = pika.PlainCredentials('sabarish', 'Password123')
parameters = pika.ConnectionParameters('rabbitmq.selfmade.ninja', 5672, 'Sabarish_hello_world', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"



channel.basic_publish(exchange='',
                    routing_key='hello',
                    body=message)
print(" [x] Sent 'Hello World!'")