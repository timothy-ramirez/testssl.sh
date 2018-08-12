import os
from redis import Redis
from rq import Queue

q = Queue(connection=Redis(host='redis-15749.c16.us-east-1-3.ec2.cloud.redislabs.com', port=15749, password='FIq4TLlk7wlFvniLQhddCGJQtzDl8Khx'))

def handle_job(data):
	print('Handling...', data)

