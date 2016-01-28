from isbndb.baseservice import BaseService
from isbndb.parsedresponse import ParsedResponse

class Publishers(BaseService):
  ''' ISBNdb API service for publishers endpoints '''

  def __init__(self):
    BaseService.__init__(self)
