import requests
from ISS.exceptions import BadLatitudeException, BadLongitudeException, BadAltitudeException, BadNumberException
from datetime import datetime


class Client:
    def __init__(self):
        self.base_url = 'http://api.open-notify.org/'

    def get_location(self):
        return requests.get('{}iss-now.json'.format(self.base_url))

    def get_pass_times(self, lat=1, lon=1, alt=1, num=1):
        response = requests.get('{}iss-pass.json?lat={}&lon={}&alt={}&n={}'.format(self.base_url, lat, lon, alt, num))
        if response.status_code == 400:
            if 'Latitude' in response.json()['reason']:
                raise BadLatitudeException('Latitude value must be between -90.0 and 90.0 degrees (cannot be 0).')
            elif 'Longitue' in response.json()['reason']:
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
            return datetime.utcfromtimestamp(response.json()['response'][0]['risetime'])

    def get_number_of_astronauts(self):
        return self.get_astronauts().json()['number']

    def get_list_of_astronaut_names(self):
        return [person['name'] for person in self.get_astronauts().json()['people']]

    def get_next_pass_duration_in_seconds(self, lat=1, lon=1, alt=1):
        response = self.get_pass_times(lat, lon, alt, 1)
        if len(response.json()['response']) == 0:
            return 'No passes found.'
        else:
            return response.json()['response'][0]['duration']

    def get_set_of_occupied_spacecraft(self):
        return set([person['craft'] for person in self.get_astronauts().json()['people']])
