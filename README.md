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
3. in your browser, open the page: [http://localhost:8000](http:localhost:8000)
4. you should see the inital data, and be able to create, update or delete any of the records

## Misconceptions
I thought I had it doing all updates via the REST API. However, I was just making calls to the DB, using the same logic the API used!

Refactored to use api.demojoyto.win.

## Learnings
One side-effect of having a web frontend and an API is the different ways the same data displays. Note how chatgpt-webapp renders users puts the fiellds in alphabetical order (email/id/name) while the raw API puts/keeps them as they are defined in the DB (id/name/email).

Notes: had to add both AWS IPs to the Cloudflare WAF to prevent 403s.

## Codebase visualization
![Visualization of the codebase](https://github.com/aaronhmiller/chatgpt-webapp/blob/diagram/diagram.svg?raw=true)
