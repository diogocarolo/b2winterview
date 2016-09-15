import os
import tweepy
import demjson
import datetime
import bottle
from bottle import Bottle, route, run, hook, template, get, response, request



#inicia variaveis de acesso twitter
cons_key = "OvfdRuq1u3iMfuYwOmJvaauad"
cons_secret = "aMrb4y7gyDwiLzeFzgUSh3af5PgYBe6Wh2oasih2AhVRFsqG0s"
access_token = "1864929535-UjtQEsaEeY7LiNao48jHKpLPqQnSfjldc766G2A"
access_token_secret = "HgIpDHq3b1hvkFA0PojzrrY0y3KSQvST0qYurPiUuBZJw"



#cria objeto para manipular a api do twitter
auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

app = Bottle();


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    

@route('/tweets',METHOD='get')
def tweets():
	tweets = api.user_timeline(id="americanascom",count=5,page=bottle.request.params.get('page'))
	imageTweet = ""
	json = []
	for t in tweets:
		if 'media' in t.entities:
			for image in  t.entities['media']:
				imageTweet = image['media_url']
		json.append({
			'text': t.text,
			'img': imageTweet,
			'imgProfile': t.user.profile_image_url,
			'name': t.user.name,
			'screen_name': "@"+t.user.screen_name,
			'replyTo': t.in_reply_to_screen_name,
			
		})
	
	tweet = demjson.encode(json)
	response.headers['Content-Type'] = 'application/json'
	return tweet


#get tweets with media
@route('/tweets-media',METHOD='get')
def tweetsImage():
	tweets = api.user_timeline(id="americanascom",count=10,page=bottle.request.params.get('page'))
	json = []
	for t in tweets:
		if 'media' in t.entities:
			for image in  t.entities['media']:
				imageTweet = image['media_url']
				json.append({
					'text': t.text,
					'img': imageTweet,
					'imgProfile': t.user.profile_image_url,
					'name': t.user.name,
					'screen_name': "@"+t.user.screen_name,
					'replyTo': t.in_reply_to_screen_name,
				})
	tweet = demjson.encode(json)
	response.headers['Content-Type'] = 'application/json'
	return tweet

@route("/info-user")
def info():
	info = api.get_user(id="americanascom")
	json = {
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
	}
	infoUser = demjson.encode(json)
	response.headers['Content-Type'] = 'application/json'
	return infoUser

@route("/trends")
def trend():
	json = []
	trends = api.trends_place(1)
	data = trends[0]
	trends = data['trends']
	for t in range(10):
		json.append({
			"name": trends[t]['name'],
			"tweet_count": trends[t]['tweet_volume'] 
		})

	infoTrends = demjson.encode(json)
	response.headers['Content-Type'] = 'application/json'
	return infoTrends


run(host='localhost', port=8080, debug=True)