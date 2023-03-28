import unittest
import app

class TestApp(unittest.TestCase):
    def test_request_dict(self):
        url = 'https://www.w3schools.com/xml/note.xml'
        response_dict = app.request_dict(url)
        self.assertIsInstance(response_dict, dict)

    def test_request_dict_error(self):
        url = 'https://www.w3schools.com/xml/note_error.xml'
        self.assertRaises(Exception, lambda: app.request_dict(url))
