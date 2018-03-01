## About

My personal Flask boilerplate. A set of defaults that works well for me!

## Setup

- Create the database (uses [Postgres](https://www.postgresql.org/download/))

        `psql -c CREATE DATABASE boilerplate;`

- Install the requirements and setup the development environment.

        `./setup.sh`

- Run the application.

        `./run.sh`

- Navigate to [localhost:8000](localhost:8000).


## Deploy to Heroku with Git

Create a [Heroku account](https://signup.heroku.com/)

Download the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

        `heroku create`
        `git push heroku master`


## License

The MIT License (MIT). Please see the [license file](LICENSE) for more information.

Forked with much appreciation from https://github.com/MaxHalford/flask-boilerplate
