import subprocess
import time
import uuid
import requests
import json

from pymongo import MongoClient


client = MongoClient('mongodb://ssl-user-1:ssl-user-1@ds119732.mlab.com:19732/ssl-test-mongo')
db = client['ssl-test-mongo']
collection = db.my_results


def handle_job(url):
	start = time.time()
	e = None
	
	try:
		head = requests.head(url, timeout=5, verify=False)
	except Exception as e:
		head = None
		
	post_head = time.time()
	
	results_file = '/tmp/{}'.format(uuid.uuid4())
	p = subprocess.Popen(['/bin/bash', './testssl.sh', '--jsonfile', '{}'.format(results_file), url])
	stdout, stderr = p.communicate()
	
	with open(results_file) as f:
		parsed_results = json.load(f)
		
	res = collection.insert_one({
		"success": True,
		"ssltest": parsed_results,
		"head": {"text": head.headers, "status": head.status_code} if head else e,
		"time": {
			"start": start,
			"post_head": post_head,
			"end": time.time()
		}
	})
	
	print('{} done with {}'.format(data, res.inserted_id))

	
	