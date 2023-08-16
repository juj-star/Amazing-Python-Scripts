import requests
import unittest
from unittest.mock import patch

def get_air_quality(city, api_key):
    url = 'http://api.waqi.info/feed/' + city + '/?token='
    main_url = url + api_key
    r = requests.get(main_url)
    return r.json()['data']

class TestAirQualityProgram(unittest.TestCase):

    @patch('requests.get')
    def test_get_air_quality(self, mock_get):
        # Mocking the API response
        mock_get.return_value.json.return_value = {
            'data': {
                'aqi': 100,
                'iaqi': {
                    'dew': {'v': 10},
                    'no2': {'v': 20},
                    'o3': {'v': 30},
                    'so2': {'v': 40},
                    'pm10': {'v': 50},
                    'pm25': {'v': 60}
                }
            }
        }

        city = 'kanpur'
        api_key = 'fake_api_key'
        
        # Call the get_air_quality function directly.
        result = get_air_quality(city, api_key)

        # Add assertions to check the correctness of the result.
        self.assertEqual(result['aqi'], 100)
        self.assertEqual(result['iaqi']['dew']['v'], 10)
        self.assertEqual(result['iaqi']['no2']['v'], 20)
        self.assertEqual(result['iaqi']['o3']['v'], 30)
        self.assertEqual(result['iaqi']['so2']['v'], 40)
        self.assertEqual(result['iaqi']['pm10']['v'], 50)
        self.assertEqual(result['iaqi']['pm25']['v'], 60)

if __name__ == '__main__':
    unittest.main()
