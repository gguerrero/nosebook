from isbndb.baseservice import BaseService
from isbndb.parsedresponse import ParsedResponse

class Categories(BaseService):
  ''' ISBNdb API service for categories endpoints '''

  def __init__(self):
    BaseService.__init__(self)
