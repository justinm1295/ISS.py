import requests
from ISS.exceptions import BadLatitudeException, BadLongitudeException, BadAltitudeException, BadNumberException
from datetime import datetime


class Client:
    def __init__(self):
        self.base_url = 'http://api.open-notify.org/'

    def get_location(self):
        return requests.get('{}iss-now.json'.format(self.base_url))

    def get_pass_times(self, lat=1, lon=1, alt=1, num=1):
        print('test2')
        response = requests.get('{}iss-pass.json?lat={}&lon={}&alt={}&n={}'.format(self.base_url, lat, lon, alt, num))
        if response.status_code == 400:
            if 'Latitude' in response.json()['reason']:
                raise BadLatitudeException('Latitude value must be between -90.0 and 90.0 degrees (cannot be 0).')
            elif 'Longitude' in response.json()['reason']:
                raise BadLongitudeException('Longitude value must be between -180.0 and 180.0 degrees (cannot be 0).')
            elif 'Altitude' in response.json()['reason']:
                raise BadAltitudeException("Altitude must be between 1 and 10,000")
            elif 'Number' in response.json()['reason']:
                raise BadNumberException("Number must be between 1 and 100")
        return response

    def get_astronauts(self):
        return requests.get('{}astros.json'.format(self.base_url))

    def get_next_pass_date(self, lat=1, lon=1, alt=1):
        response = self.get_pass_times(lat, lon, alt, 1)
        if len(response.json()['response']) == 0:
            return 'No passes found.'
        else:
            return datetime.utcfromtimestamp(response.json()['response'][0]['risetime']).strftime('%B %d, %Y at %I:%M:%S %p UTC')


def main():
    client = Client()
    client.get_next_pass_date()


if __name__ == "__main__":
    main()
