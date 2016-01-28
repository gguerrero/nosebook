import xml.etree.ElementTree
import json
import yaml

class ParsedResponse:
  ''' Parse an HTTPResponseobject to extract basic info and deserialize body object. '''

  def __init__(self, response, responseformat):
    self.httpresponse = response
    self.format       = responseformat
    self.status       = self.httpresponse.status
    self.reason       = self.httpresponse.reason
    self.body         = self.parse(responseformat)

  def ok(self):
    ''' The API always return 200 status, so body should be checked ''' 
    return self.status == 200

  def parse(self, responseformat):
    ''' Returns response body depending on responseformat '''
    decodedresponse = self.httpresponse.read().decode()
    try:
      if callable(getattr(self, self.format)):
        return getattr(self, self.format).__call__(decodedresponse)
      else:
        return decodedresponse
    except AttributeError:
      return decodedresponse


  def geterrormessage(self):
    ''' Returns error message in case it exist '''
    try:
      methodname = self.format+"errormessage"
      if callable(getattr(self, methodname)):
        return getattr(self, methodname).__call__()
      else:
        return None
    except AttributeError:
      return None    

  # Methods related to valid formats (parsing and error messages methods)
  def xml(self, decodedresponse):
    return xml.etree.ElementTree.fromstring(decodedresponse)

  def xmlerrormessage(self):
    error = self.body.find('error')
    return (error.text if error else None)

  def json(self, decodedresponse):
    return json.loads(decodedresponse)

  def jsonerrormessage(self):
    return self.body.get('error')

  def yaml(self, decodedresponse):
    return yaml.load(decodedresponse)

  def yamlerrormessage(self):
    return self.body.get('error')
