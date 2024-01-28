# Webform that updates DB

Assumes a pre-existing REST API & running Postgres DB

I had an existing project [crud-app](https://github.com/aaronhmiller/crud-app) that has an Express-based CRUD API that uses Postgres.

I asked ChatGPT:

1. `write me a web page that interacts with a REST API backend that uses Postgres DB`
2. `now show me how to create a web form that allows me to edit the data using the REST API`

It told me to install Flask (Python framework) and gave me app.py & index.html & style.css for a webform that interacted with my Postgres DB using my REST API.

## Usage

1. Fire up the crud-app docker compose stack, from its directory, `docker compose up -d`
2. from this project's directory, run `python3 app.py`
3. in your browser, open the page: [http://127.0.0.1:5000/](http:127.0.0.1:5000)
4. you should see the inital data, and be able to update any of the records

## To-do

Add ability to CREATE new records. This will need POST implemented in the web page (there's a REST call ready to go already)
