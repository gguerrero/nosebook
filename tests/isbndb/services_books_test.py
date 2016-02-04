import os
import sys
import unittest

## Append local directory for load modules
sys.path.append(os.getcwd())

import isbndb
from   isbndb import *
import isbndb.services
from   isbndb.services import *


class BooksTestCase(unittest.TestCase):

  def setUp(self):
    self.connection = isbndb.services.books.Books()

  def tearDown(self):
    self.connection.close()

  def test_getbook(self):
    response = self.connection.getbook('invalid_slug_or_isbn')
    self.assertEqual(response.status, 200)
    self.assertNotEqual(response.geterrormessage(), None)

    response = self.connection.getbook('el_quijote')
    self.assertEqual(response.status, 200)
    self.assertEqual(response.geterrormessage(), None)

  def test_getbooks(self):
    response = self.connection.getbooks('El Quijote')
    self.assertGreater(response.body['result_count'], 0)

  def test_getbooks_by_author_name(self):
    response = self.connection.getbooks('Cervantes', 'author_name')
    self.assertEqual(response.body['index_searched'], 'author_name')
    self.assertGreater(response.body['result_count'], 0)



if __name__ == '__main__':
  unittest.main()
