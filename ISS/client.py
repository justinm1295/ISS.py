from ISS.exceptions import *
import requests
from datetime import datetime


class Client:
    def __init__(self):
        self.base_url = 'http://api.open-notify.org/'

    def get_location(self):
        response = requests.get(f'{self.base_url}iss-now.json')
        if response.status_code is not 200:
            raise LocationFailureException('Unable to get current location.')
        return response.json()['iss_position']

    def get_pass_times(self, lat=1.0, lon=1.0, alt=1.0, num=1):
        response = requests.get(f'{self.base_url}iss-pass.json?lat={lat}&lon={lon}&alt={alt}&n={num}')
        if response.status_code is not 200:
            if 'Latitude' in response.json()['reason']:
                raise BadLatitudeException(f'Latitude value must be between -90.0 and 90.0 degrees (cannot be 0). Entered: {lat}')
            elif 'Longitue' in response.json()['reason']:
                raise BadLongitudeException(f'Longitude value must be between -180.0 and 180.0 degrees (cannot be 0). Entered: {lon}')
            elif 'Altitude' in response.json()['reason']:
                raise BadAltitudeException(f"Altitude must be between 1 and 10,000. Entered: {alt}")
            elif 'Number' in response.json()['reason']:
                raise BadNumberException(f"Number must be between 1 and 100. Entered: {num}")
        return response.json()['response']

    def get_astronauts(self):
        response = requests.get(f'{self.base_url}astros.json')
        if response.status_code is not 200:
            raise AstronautFailureException('Unable to get current astronauts.')
        return response.json()['people']

    def get_date_of_next_pass(self, lat=1.0, lon=1.0, alt=1.0):
        dates = self.get_pass_times(lat, lon, alt, 1)
        if len(dates) == 0:
            return 'No passes found.'
        else:
            return datetime.utcfromtimestamp(dates[0]['risetime'])

def main():
    client = Client()
    print(client.get_date_of_next_pass(10.0, 20, 5,))

if __name__ == "__main__":
    main()