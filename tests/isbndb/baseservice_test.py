import os
import sys
import unittest

## Append local directory for load modules
sys.path.append(os.getcwd())

import isbndb
from   isbndb import *
import isbndb.services
from   isbndb.services import *


class BaseServiceTestCase(unittest.TestCase):

  def setUp(self):
    self.connection = isbndb.baseservice.BaseService()

  def tearDown(self):
    self.connection.close()

  def test_connection(self):
    self.assertEqual(self.connection.host, isbndb.HOSTNAME)

  def test_basepath(self):
    self.assertEqual(self.connection.basepath(), "/api/v2/json/"+isbndb.APIKEY)
    self.connection.format = 'xml'
    self.assertEqual(self.connection.basepath(), "/api/v2/xml/"+isbndb.APIKEY)

  def test_cgiparams(self):
    params = {
      'foo':     "FOO",
      'bar':     "BAR",
      'foo_bar': "FOO BAR"
    }
    self.assertIn(self.connection.cgiparams(params), ["?foo=FOO&bar=BAR&foo_bar=FOO%20BAR",
                                                      "?foo=FOO&foo_bar=FOO%20BAR&bar=BAR",
                                                      "?bar=BAR&foo=FOO&foo_bar=FOO%20BAR",
                                                      "?bar=BAR&foo_bar=FOO%20BAR&foo=FOO",
                                                      "?foo_bar=FOO%20BAR&foo=FOO&bar=BAR",
                                                      "?foo_bar=FOO%20BAR&bar=BAR&foo=FOO"])


if __name__ == '__main__':
  unittest.main()
