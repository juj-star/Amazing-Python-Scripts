import unittest
from unittest.mock import patch
from script import display_content

class TestDisplayContent(unittest.TestCase):

    @patch('script.requests.get')
    def test_success(self, mock_get):
        # Simulating a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html><body><p class="test">Hello, World!</p></body></html>'

        url = 'http://example.com'
        selector = '.test'
        result = display_content(url, selector)
        
        # Check that the content was correctly extracted
        self.assertEqual(result, ['Hello, World!'])

    @patch('script.requests.get')
    def test_failed_fetch(self, mock_get):
        # Simulating a failed response
        mock_get.return_value.status_code = 404

        url = 'http://example.com'
        selector = '.test'
        result = display_content(url, selector)
        
        # Check that the function returns None in case of a failed response
        self.assertIsNone(result)

    @patch('script.requests.get')
    def test_request_exception(self, mock_get):
        # Simulating an exception during the request
        mock_get.side_effect = requests.exceptions.RequestException("An exception")

        url = 'http://example.com'
        selector = '.test'
        result = display_content(url, selector)

        # Check that the function returns None in case of an exception
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
