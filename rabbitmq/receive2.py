import pika


#it uses AMQP to communicate 
credentials = pika.PlainCredentials('sabarish', 'Password123')
parameters = pika.ConnectionParameters('rabbitmq.selfmade.ninja', 5672, 'Sabarish_hello_world', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()