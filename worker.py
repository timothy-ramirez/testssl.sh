from pymongo import MongoClient


client = MongoClient('mongodb://ssl-user-1:ssl-user-1@ds119732.mlab.com:19732/ssl-test-mongo')
db = client['ssl-test-mongo']
collection = db.my_results


def handle_job(data):
	res = collection.insert_one({
		"success": True,
		"data": data
	})
	
	print('{} done with {}'.format(data, res.inserted_id))

	
	
handle_job('Some site')