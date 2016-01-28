import os

# Loaded modules when * is called
__all__  = ["parsedresponse", "book", "author"]

# Constants, maybe used with ENV vars
HOSTNAME = os.getenv('ISBNDB_HOSTNAME', 'isbndb.com')
APIKEY   = os.getenv('ISBNDB_HOSTNAME', '45ATS15S')
