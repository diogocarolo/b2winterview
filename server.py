import os
import tweepy
import sys
import demjson
from bottle import route, run, template, get, static_file

# bottle.TEMPLATE_PATH.insert(0, '/public/templates/')

@route('/')
def index():
	cons_key = "OvfdRuq1u3iMfuYwOmJvaauad"
	cons_secret = "aMrb4y7gyDwiLzeFzgUSh3af5PgYBe6Wh2oasih2AhVRFsqG0s"
	access_token = "1864929535-UjtQEsaEeY7LiNao48jHKpLPqQnSfjldc766G2A"
	access_token_secret = "HgIpDHq3b1hvkFA0PojzrrY0y3KSQvST0qYurPiUuBZJw"

	json = []
	auth = tweepy.OAuthHandler(cons_key, cons_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	tweets = api.user_timeline(id="americanascom",count=200)
	imageTweet = ""

	for t in tweets:
		if 'media' in t.entities:
			for image in  t.entities['media']:
				imageT = image['media_url']
		json.append({
			'texto': t.text,
			'img': imageTweet
		})
		
	tweet = demjson.encode(json)
	return tweet
	
	
run(host='localhost', port=8080, debug=True)