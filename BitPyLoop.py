import urllib, json
import datetime
import time
def getPrice():
	url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	parsed_json = json.loads(json.dumps(data))
	currentPrice = float(parsed_json[u'data'][u'amount'])
	return currentPrice

dataFileWriteJSON = open("Tree.json","a")
currentPrice = getPrice()
dataFileWriteJSON.write("{"+'"'+str(currentPrice)+'"'+"}"+'\n')




