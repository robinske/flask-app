## About

My personal Flask boilerplate. A set of defaults that works well for me!

## Setup

### Vanilla

- Install the requirements and setup the development environment.

	`make install && make dev`

- Create the database.

	`python manage.py initdb`

- Run the application.

	`python manage.py runserver`

- Navigate to `localhost:5000`.


### Virtual environment

``
pip install virtualenv
virtualenv venv
venv/bin/activate
make install
make dev
python manage.py initdb
python manage.py runserver
``

## License

The MIT License (MIT). Please see the [license file](LICENSE) for more information.

Forked with much appreciation from https://github.com/MaxHalford/flask-boilerplate
