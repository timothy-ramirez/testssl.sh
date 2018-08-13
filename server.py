import os
from redis import Redis
from rq import Queue
from worker import handle_job
q = Queue(connection=Redis(host='redis-15749.c16.us-east-1-3.ec2.cloud.redislabs.com', port=15749, password='FIq4TLlk7wlFvniLQhddCGJQtzDl8Khx'))




result = q.enqueue(
		 handle_job, 'https://nvie.com/', timeout=60*20)
		 
print('Done!', result)		 
			 