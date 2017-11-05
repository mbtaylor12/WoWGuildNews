import json
import urllib

API_INFO=open("API_INFO.txt", "r")

REALMNAME=API_INFO.readline()[11:].replace(" ", "%20")
GUILDNAME=API_INFO.readline()[11:].replace(" ", "%20")
LOCALE=API_INFO.readline()[7:]
APIKEY=API_INFO.readline()[7:]

API_INFO.close()

def getLatestNews():
	url="https://us.api.battle.net/wow/guild/" + REALMNAME + "/" + GUILDNAME + "?fields=news&locale=" + LOCALE + "&apikey=" + APIKEY
	response=urllib.urlopen(url)
	jsonData=json.loads(response.read())
	newsData=jsonData["news"][0]

	character=newsData["character"]
	message=character

	if(newsData["type"]=="playerAchievement"):
		achievementTitle=newsData["achievement"]["title"]
		message = message + " earned " + achievementTitle
	elif("item" in newsData["type"]):
		item=newsData["itemId"]
		message = message + " has received the item " + str(item)


	return message