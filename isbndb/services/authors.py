from isbndb.baseservice import BaseService
from isbndb.parsedresponse import ParsedResponse

class Authors(BaseService):
  ''' ISBNdb API service for authors endpoints '''

  def __init__(self):
    BaseService.__init__(self)
