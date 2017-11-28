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
  ```
* Launch the Redis docker container.
  ```bash
  $ make docker_up
  ```
* Launch the Celery worker.  
  **NOTE** - The celery worker holds the terminal so run it in a separate terminal which also has the project's python enviroment. Also keep in mind to always have only one terminal running a worker at a time.
  ```bash
  $ make celery_up
  ```

#### Recreate Environment
Assuming you are already inside the enviroment, just run the following command to recreate the python enviroment and start docker and start the celery worker.

**NOTE**: Run it in a separate terminal since the celery worker holds the terminal.
```bash
$ make recreate_env
```


# Usage
1. First get the celery worker to start by running ANY ONE of the following commands in a separate terminal.
  ```bash
  # Run one of these commands in another terminal
  $ make celery_up
  (OR)
  $ make recreate_env
  ```
2. Then run the following command in another terminal and then open `localhost:9999` on your browser.
  ```bash
  $ make run_server
  ```
