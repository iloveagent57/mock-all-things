import unittest

from .common import MockDateTime


class MockDateTimeTest(unittest.TestCase):
    def test_utcnow(self):
        self.assertEqual(MockDateTime.NOW, MockDateTime.utcnow())

    def test_strptime(self):
        self.assertEqual(MockDateTime.NOW, MockDateTime.strptime('2015-01-01', '%Y-%m-%d'))

    def test_utcfromtimestamp(self):
        self.assertEqual(MockDateTime.NOW, MockDateTime.utcfromtimestamp(1234567890))
