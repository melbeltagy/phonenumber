## Project Setup

* `python -m venv venv` to set up virtual environment to run your application within.
* `source venv/bin/activate` to start the virtual environment.
    * Look in the bin directory to choose the correct `activate` script. For example, if you use the fish shell you would use activate.fish.
    * To exit the virtual environment, run `deactivate`
    * You need to enter the virtual environment every time you work on the application.
* Install project dependencies: `make release`
    * If you are a developer you must run `make development`


## Unit tests

To run the unit test, use `make test`

## Code Lint
Run `make lint` to generate lint report
