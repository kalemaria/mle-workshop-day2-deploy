MODEL_PATH = ./models/model-2022-01.bin
export MODEL_PATH

VERSION = 2022-01-v01
export VERSION

run:
	pipenv run python duration_prediction_serve/serve.py

docker_build:
	docker build -t duration-prediction:latest . 

docker_run: docker_build
	docker run -it -p 9697:9696 --rm duration-prediction:latest
