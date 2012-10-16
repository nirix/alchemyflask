AlchemyFlask
============

AlchemyFlask is an example Flask app that uses SQLAlchemy for the database.

Setup
-----

To setup the example, edit the `settings.yml` file and set your database
information.

To do so, change the `database` URL to

    [driver]://[username]:[password]@[server]/[database_name]

Then run `python tables.py` and insert a few rows, then run `python app.py`
to run the example app.
