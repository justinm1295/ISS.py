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
# Returns JSON object containing the next *num* passes for the specified *lat*, *lon*, and *alt*.

get_astronauts()
# Returns JSON object containing the astronauts currently in orbit.
```