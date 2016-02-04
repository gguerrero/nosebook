# NoseBook
Basic user interface app for search, list and show details about books.

## Requirements
- [Python 3](https://www.python.org/download/releases/3.0/) or higher
- [PyYAML](http://pyyaml.org/wiki/LibYAML)

## The ISBNdb services
All the services for retriving data from the ISBNdb repository are coded under the
[**isbndb**](https://github.com/gguerrero/nosebook/tree/master/isbndb) package:

- ```isbndb/__init__.py``` file read environment variables required to connect to the isbndb.com services.
There are ```ISBNDB_HOSTNAME``` and ```ISBNDB_APIKEY```. These vars have default values.

## Unit Testing
For running test just run this command (Python3 or more is required):

```bash
python3.4 $(find tests -type f)
```

Or if you want to run indivual files as:

```bash
python3.4 tests/isbndb/baseservice_test.py
```
