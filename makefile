install:
	@echo 'instalando dependencias python'
	pip install tweepy
	pip install demjson
	pip install flask
	pip install flask-cors
	pip install flickrapi
	@echo 'levantando servers'
	cd /public
	python -m SimpleHTTPServer &
	python server-flask.py &
	google-chrome 127.0.0.1:8000/public

