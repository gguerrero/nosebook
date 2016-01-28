from isbndb.baseservice import BaseService
from isbndb.parsedresponse import ParsedResponse

class Prices(BaseService):
  ''' ISBNdb API service for books endpoints '''

  def __init__(self):
    BaseService.__init__(self)

  def getprices(self, book_isbn_or_slug, optparams = {}):
    url = self.basepath()+"/prices/"+str(book_isbn_or_slug)+cgiparams(optparams)
    self.request("GET", url)
    return ParsedResponse(self.getresponse(), self.format)
