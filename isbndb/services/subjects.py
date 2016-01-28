from isbndb.baseservice import BaseService
from isbndb.parsedresponse import ParsedResponse

class Subjects(BaseService):
  ''' ISBNdb API service for subjects endpoints '''

  def __init__(self):
    BaseService.__init__(self)
