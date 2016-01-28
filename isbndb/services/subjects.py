from isbndb.baseservice import BaseService
from isbndb.parsedresponse import ParsedResponse

class Subjects(BaseService):
  ''' ISBNdb API service for subjects endpoints '''

  def __init__(self):
    BaseService.__init__(self)

  def getsubject(self, subjectid, optparams = {}):
    url = self.basepath()+"/subject/"+str(subjectid)+cgiparams(optparams)
    self.request("GET", url)
    return ParsedResponse(self.getresponse(), self.format)

  def getsubjects(self, subjectname, optparams = {}):
    params = {'q': subjectname}
    params.update(optparams)
    url = self.basepath()+"/subjects"+self.cgiparams(params)
    self.request("GET", url)
    return ParsedResponse(self.getresponse(), self.format)
