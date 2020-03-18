## Project Setup
* `python -m venv venv` to set up virtual environment to run your application within.
* `source venv/bin/activate` to start the virtual environment.
    * Look in the bin directory to choose the correct `activate` script. For example, if you use the fish shell you would use activate.fish.
    * To exit the virtual environment, run `deactivate`
    * You need to enter the virtual environment every time you work on the application.
* Install project dependencies: `pip install -r requirements.txt`
    * If you are a developer you must also run `pip install -r requirements-dev.txt`

## Unit tests
#### Python
To run the unit test, use `python -m unittest`
#### Make
To run the unit test, use `make test`

## Code Lint
#### Python only
* For type checking, run: `mypy .\phonenumber.py .\tests.py`
* For style check, run: `flake8 .\phonenumber.py .\tests.py`
#### Make
Run `make lint`
