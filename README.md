# Flask Celery Job Status
A basic project for displaying the status of job/tasks using flask, celery and redis.

# Development Installation

#### First Time Environment Creation
* Clone the project and `cd` into project.
* Edit dev-environment.yml
* Enable Anaconda3
* Create the Anaconda3 envionment
	```bash
	conda env create --force -f dev_environment.yml
	source activate flask-celery-job-status
	pip install -e .
	make docker_up
	make celery_up
	```

#### Recreate Environment
Assuming you are already inside the enviroment, just run the following command to recreate the python enviroment and start docker and celery.
```bash
make recreate_env
```


# Test
To run the tests:
```bash
make test
```


# Usages
Run the following command and then open `localhost:9999` on your browser.
```bash
make run_server
```