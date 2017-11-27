PROJECT := flask-celery-job-status
.DEFAULT_GOAL := help
DEFAULT_PORT := 9999
DEFAULT_WORKERS := 1
port := $(DEFAULT_PORT)
workers := $(DEFAULT_WORKERS)

help:                ## Show available options with this Makefile
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean:          ## Remove all the docker containers.
clean:
	cd docker && docker-compose down -v

docker_up:			# Get docker up and running
docker_up:  clean
	cd docker && \
	docker-compose up -d && \
	chmod +x ./wait-for-it.sh && \
	./wait-for-it.sh localhost:6379 -- echo "Docker containers up and running!"

recreate_env:        ## Recreate the docker environment and python anaconda environment.
recreate_env:    docker_up
	conda env create --force -f dev_environment.yml && \
	pip install -e .

run_server:            ## Run Server
run_server:
	gunicorn --workers=$(workers) -b 0.0.0.0:$(port) --log-level DEBUG --reload "flask_celery_job_status.server:create_app()"
