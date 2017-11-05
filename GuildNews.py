import json
import urllib

API_INFO=open("API_INFO.txt", "r")

REALMNAME=API_INFO.readline()[11:].replace(" ", "%20")
GUILDNAME=API_INFO.readline()[11:].replace(" ", "%20")
LOCALE=API_INFO.readline()[7:]
APIKEY=API_INFO.readline()[7:]

API_INFO.close()

def resolveItemQuality(itemID):
	return{
		0 : "poor",
		1 : "common",
		2 : "uncommon",
		3 : "rare",
		4 : "epic",
		5 : "legendary",
		6 : "artifact",
		7 : "heirloom",
		8 : "WoW Token"
	}[itemID]

def resolveItemInfo(itemID):
	url="https://us.api.battle.net/wow/item/" + str(itemID) + "?locale=" + LOCALE + "&apikey=" + APIKEY
	response=urllib.urlopen(url)
	jsonData=json.loads(response.read())

	itemInfo={}

	itemInfo["name"]=jsonData["name"]
	itemInfo["quality"]=resolveItemQuality(jsonData["quality"])

	return itemInfo


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
		itemInfo=resolveItemInfo(item)
		message = message + " has received the " + str(itemInfo["quality"]) + " item " + itemInfo["name"]


	return message

print getLatestNews()