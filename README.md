[![Build status](https://travis-ci.org/justinm1295/ISS.py.svg?master)](https://travis-ci.org/justinm1295)

ISS.py
======

Information
-----------
This is a work in progress, and will be updated iteratively as new features are finished.
Documentation will be added as necessary.

Contributions in the form of Issues, Pull Requests, and other appropriate methods is encouraged!

Key Features
------------
- Provides an easy-to-use Python wrapper for the [Open Notify ISS APIs](http://open-notify.org/)
- 100% coverage of the aforementioned API, as well as added features for enhanced usage.
- Code testing performed by [Pytest](https://pytest.org/en/latest/)

Documentation
-------------
### Client

```python 
get_location()
# Returns dict containing the current latitude and longitude of the ISS.
# If unable to retrieve the location for any reason, returns a LocationFailureException

get_pass_times(lat=1, lon=1, alt=1, num=1)
# Returns a list of dicts containing the next num passes for the specified lat, lon, and alt.
# If lat, lon, alt, or num are invalid, returns a Bad<Latitude, Longitude, Altitude, Number>Exception.

get_astronauts()
# Returns a list of dicts containing the astronauts currently in orbit.
# If unable to retrieve the astronauts for any reason, returns a AstronautFailureException

get_date_of_next_pass(lat=1, lon=1, alt=1)
# Returns the UTC datetime of the next pass for the specified lat, lon, and alt OR 'No passes found."
# If lat, lon, or alt are invalid, returns a Bad<Latitude, Longitude, Altitude>Exception
```

### Examples

```python
from ISS import Client


client = Client()

# Get the current location of the ISS.
print(client.get_location())
# {'longitude': '-63.5005', 'latitude': '16.5390'}

# Find the number of astronauts in space.
print(len(client.get_astronauts()))
# 6

# Get the names of the astronauts in space.
print([person['name'] for person in client.get_astronauts()])
# ['Alexey Ovchinin', 'Nick Hague', 'Christina Koch', 'Alexander Skvortsov', 'Luca Parmitano', 'Andrew Morgan']

# Get date of next pass.
print(client.get_date_of_next_pass(10.0, 20, 5))
# 2019-07-28 22:39:25
```
