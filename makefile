install:
	@echo 'instalando dependencias python'
	pip install -r requirements.txt

	@echo 'levantando servers'
	cd ./public
	python -m SimpleHTTPServer &
	python server-flask.py &

