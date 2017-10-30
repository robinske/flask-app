## About

My personal Flask boilerplate. A set of defaults that works well for me!

## Setup

### Vanilla

- Install the requirements and setup the development environment.

	`./setup.sh`

- Run the application.

	`./run.sh`

- Navigate to `localhost:8000`.


### Virtual environment

```
pip install virtualenv
virtualenv venv
venv/bin/activate
make install
make dev
python manage.py initdb
python manage.py runserver
```

## License

The MIT License (MIT). Please see the [license file](LICENSE) for more information.

Forked with much appreciation from https://github.com/MaxHalford/flask-boilerplate
