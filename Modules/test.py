
import unittest
from script import check_connectivity

class TestStringMethods(unittest.TestCase):

  def test_google_dn(self):
      self.assertEqual(check_connectivity('http://www.google.com'), True)

  def test_personal_dn(self):
	self.assertEqual(check_connectivity('http://www.dkroell.com'), True)

  def test_false_dn(self):
	self.assertEqual(check_connectivity('http://128.144'), False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)


