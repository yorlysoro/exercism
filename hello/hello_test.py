import unittest
from hello import Hello

class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(Hello(), "Hello, World!")
