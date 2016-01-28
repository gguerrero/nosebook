import isbndb
from   http.client import HTTPConnection


class BaseService(HTTPConnection):
  ''' ISBNdb API service base '''

  def __init__(self):
    self.format   = 'json'
    self.response = {}
    HTTPConnection.__init__(self, isbndb.HOSTNAME)

  def basepath(self):
    return "/api/v2/"+self.format+"/"+isbndb.APIKEY
