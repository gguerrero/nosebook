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
To run the tests:

```bash
python3.4 tests/isbndb_baseservice_test.py
python3.4 tests/isbndb_services_books_test.py
```
