import http.client
from http.client import HTTPConnection

class BookService(HTTPConnection):
  '''
  Connect with ISBNdb API service
  '''
  def __init__(self):
    self.format   = 'json'
    self.api_key  = '45ATS15S'
    self.api_path = "/api/v2/"+self.format+"/"+self.api_key
    HTTPConnection.__init__(self, "isbndb.com")

  def books(self):
    self.connect()
    self.request("GET", self.api_path+"/books")
    return self.getresponse()

  def book(self, book_id_or_name):
    pass

if __name__ == "__main__":
  service  = BookService()
  response = service.books()
  print(response.status, response.reason)
  print(response.read())
