import os
import tweepy
import sys
import demjson
import datetime
from bottle import route, run, template, get, static_file


#inicia variaveis de acesso
cons_key = "OvfdRuq1u3iMfuYwOmJvaauad"
cons_secret = "aMrb4y7gyDwiLzeFzgUSh3af5PgYBe6Wh2oasih2AhVRFsqG0s"
access_token = "1864929535-UjtQEsaEeY7LiNao48jHKpLPqQnSfjldc766G2A"
access_token_secret = "HgIpDHq3b1hvkFA0PojzrrY0y3KSQvST0qYurPiUuBZJw"

#cria objeto para manipular a api do twitter
auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

json = []

#get tweets
@route('/tweets')
def tweets():
	tweets = api.user_timeline(id="americanascom",count=200)
	imageTweet = ""

	for t in tweets:
		if 'media' in t.entities:
			for image in  t.entities['media']:
				imageTweet = image['media_url']
		json.append({
			'texto': t.text,
			'img': imageTweet
		})
		
	tweet = demjson.encode(json)
	return tweet

#get tweets with media
@route('/tweetsMedia')
def tweetsImage():
	tweets = api.user_timeline(id="americanascom",count=200)
	for t in tweets:
		if 'media' in t.entities:
			for image in  t.entities['media']:
				imageTweet = image['media_url']
				json.append({
					'text': t.text,
					'img': imageTweet
				})
	tweet = demjson.encode(json)
	return tweet

@route("/infoUser")
def info():
	info = api.get_user(id="americanascom")
	json.append({
		"name": info.name, 
		"description": info.description,
		"location": info.location,
		"followers_count": info.followers_count,
		"friends_count": info.friends_count,
		"likes": info.favourites_count,
		"month": info.created_at.strftime("%B"),
		"year": info.created_at.year,
		"tweets": info.statuses_count,
		"screen_name": "@"+info.screen_name,
		"img_background": info.profile_banner_url,
		"profile_image_url": info.profile_image_url
	})
	infoUser = demjson.encode(json)
	return infoUser

@route("/trend")
def trend():
	trends = api.trends_place(1)
	data = trends[0]
	trends = data['trends']
	for t in range(10):
		json.append({
			"name": trends[t]['name'],
			"tweet_count": trends[t]['tweet_volume'] 
		})

	infoTrends = demjson.encode(json)
	return infoTrends

run(host='localhost', port=8080, debug=True)