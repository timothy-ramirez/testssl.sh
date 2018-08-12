from pymongo import MongoClient


client = MongoClient('mongodb://ssl-test-user:timothy.ramirez123!@ds119732.mlab.com:19732/ssl-test-mongo')
db = client.ssl_test_db_1
collection = db.results


def handle_job(data):
	res = collection.insert_one({
		"success": true,
		"data": data
	})
	
	print('{} done with {}'.format(data, res.inserted_id))
