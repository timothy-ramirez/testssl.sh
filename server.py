import os
from redis import Redis
from rq import Queue
from worker import handle_job
q = Queue(connection=Redis(host='redis-15749.c16.us-east-1-3.ec2.cloud.redislabs.com', port=15749, password='FIq4TLlk7wlFvniLQhddCGJQtzDl8Khx'))


items = """
Ads.mopub.com
cm.ushareit.com
soma.smaato.net
ads.rubiconproject.com
m.addthis.com
s7.addthis.com
Adnxs.com
me-cdn.effectivemeasure.net
adsrvr.org
app.adjust.com 
app-measurement.com
Scorecardresearch.com
casalemedia.com
askfm.adspirit.de
alwatanvoice.com
shobiddak.com
yasour.org
www.xnxx.com
www.xvideos.com
m.xhamster.com
shahid.mbc.net
us-u.openx.net
platform.twitter.com
"""

for x in items.strip().split():
	
	result = q.enqueue(handle_job, 'https://{}'.format(x), timeout=60*20)
	print("submitting {} -> {}".format(x, result))