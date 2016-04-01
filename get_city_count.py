import json
import gzip
from operator import itemgetter


f = gzip.open('./outputbig.gz','r')

cities = {}

for line in f:
	#parse into json
	try:
		cline = json.loads(line)
	except:
		"whoops!"
	#get a count of visits by city
	if 'cy' in cline:
		city = cline['cy']
		if city in cities:
			cities[city] +=1
		else:
			cities[city] = 1
 	

sorted_cities = sorted(cities.items(), key=itemgetter(1))
ln = len(sorted_cities)
print sorted_cities[ln-5:ln]
f.close()

