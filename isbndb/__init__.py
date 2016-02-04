import os

# Loaded modules when * is called
__all__  = [
  "baseservice",
  "parsedresponse",
  "services.authors",
  "services.books",
  "services.categories",
  "services.prices",
  "services.publishers",
  "services.subjests"
]

# Constants, maybe used with ENV vars
HOSTNAME = os.getenv('ISBNDB_HOSTNAME', 'isbndb.com')
APIKEY   = os.getenv('ISBNDB_APIKEY',   '45ATS15S')
