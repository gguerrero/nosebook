from isbndb.baseservice import BaseService
from isbndb.parsedresponse import ParsedResponse

class Book(BaseService):
  ''' ISBNdb API service for books endpoints '''

  def __init__(self):
    BaseService.__init__(self)
    
  def getbook(self, book_isbn_or_slug):
    self.request("GET", self.basepath()+"/book/"+str(book_isbn_or_slug))
    return ParsedResponse(self.getresponse(), self.format)

  def getbooks(self, query, index = None):
    
    self.request("GET", self.basepath()+"/books")
    return ParsedResponse(self.getresponse(), self.format)
