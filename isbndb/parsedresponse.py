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

  def parse(self, responseformat):
    '''Return response body depending on responseformat'''
    decodedresponse = self.httpresponse.read().decode()
    try:
      if callable(getattr(self, self.format)):
        return getattr(self, self.format).__call__(decodedresponse)
      else:
        return decodedresponse
    except AttributeError:
      return decodedresponse

  def xml(self, decodedresponse):
    return xml.etree.ElementTree.fromstring(decodedresponse)

  def json(self, decodedresponse):
    return json.loads(decodedresponse)

  def yaml(self, decodedresponse):
    return yaml.load(decodedresponse)

  def is_ok(self):
    ''' The API always return 200 status, so body should be checked ''' 
    return self.status == 200

  def errormessage(self):
    ''' Error message in case it exist '''
    # return self.body['error']
    # return self.body.find('error').text
