ISS.py
======

Information
-----------
This is a work in progress, and will be updated iteratively as new features are finished.
Documentation will be added as necessary.

Key Features
------------
- Provides an easy-to-use Python wrapper for the `Open Notify ISS APIs <http://open-notify.org/>`_
- 100% coverage of the aforementioned API, as well as added features for enhanced usage.
- Code testing performed by `Pytest <https://pytest.org/en/latest/>`_

Documentation
-------------
### Client

```python 
get_location()
# Returns JSON object containing the current position of the ISS.

get_pass_times(lat=1, lon=1, alt=1, num=1)
# Returns JSON object containing the next *num* passes for the specified _lat_, _lon_, and _alt_.

get_astronauts()
# Returns JSON object containing the astronauts currently in orbit.

get_next_pass_date(lat=1, lon=1, alt=1)
# Returns datetime object of the next pass for the specified _lat_, _lon_, and _alt_, OR "No passes found."

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
```