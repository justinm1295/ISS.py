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
# Returns JSON object containing the next *num* passes for the specified lat, lon, and alt.
# If lat, lon, alt, or num are invalid, returns a Bad<Latitude, Longitude, Altitude, Number>Exception.

get_astronauts()
# Returns JSON object containing the astronauts currently in orbit.

get_next_pass_date(lat=1, lon=1, alt=1)
# Returns datetime object of the next pass for the specified lat, lon, and alt, OR 'No passes found.'

get_next_pass_duration_in_seconds(lat=1, lon=1, alt=1)
# Returns the duration (seconds) of the next pass for the specified lat, lon, and alt, OR 'No passes found.'

get_number_of_astronauts()
# Returns the number of astronauts currently in orbit.

get_list_of_astronaut_names()
# Returns a list containing the names of the astronauts currently in orbit.

get_set_of_occupied_spacecraft()
# Returns a set with the names of the spacecraft currently occupied.
```