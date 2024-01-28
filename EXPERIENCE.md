# Asked ChatGPT:
```
write me a web page that interacts with a REST API backend that uses Postgres DB
```

It gave me the guidance to create app.py, index.html, and style.css

1. It missed (which caused a Jinja error) to create a Templates directory and put the index.html file in it.
2. After that, it needed connection info for the DB (which it does mention)
3. It expects the REST API and DB to be created separately.
4. After that, it needed to know the database table name (it threw a pefect error on this)

```
now show me how to create a web form that allows me to edit the data using the REST API
```

5. After that, had to ask again how to add updates (PUT) and follow that
6. Had to google how to fix Jinja2 error on stylesheet not loading

7. Had to figure out how to add `+ id` to my URL for PUT for one of the suggested functions
