from isbndb.baseservice import BaseService
from isbndb.parsedresponse import ParsedResponse

class Books(BaseService):
  ''' ISBNdb API service for books endpoints '''

  def __init__(self):
    BaseService.__init__(self)
    
  def getbook(self, book_isbn_or_slug, optparams = {}):
    url = self.basepath()+"/book/"+str(book_isbn_or_slug)+self.cgiparams(optparams)
    self.request("GET", url)
    return ParsedResponse(self.getresponse(), self.format)

  def getbooks(self, query, index = None, optparams = {}):
    params = {'q': query, 'i': index}
    params.update(optparams)
    url = self.basepath()+"/books"+self.cgiparams(params)
    self.request("GET", url)
    return ParsedResponse(self.getresponse(), self.format)
