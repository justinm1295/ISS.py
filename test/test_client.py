from ISS import Client
from ISS.exceptions import *
import pytest
from datetime import datetime


class TestClient:

    def test_get_location(self):
        client = Client()
        response = client.get_location()
        assert isinstance(response, dict)

    def test_get_pass_times(self):
        client = Client()
        response = client.get_pass_times()
        assert isinstance(response, list)

    def test_get_astronauts(self):
        client = Client()
        response = client.get_astronauts()
        assert isinstance(response, list)

    def test_get_pass_times_bad_latitude(self):
        client = Client()
        with pytest.raises(BadLatitudeException):
            client.get_pass_times(0, 1, 1, 1)

    def test_get_pass_times_bad_longitude(self):
        client = Client()
        with pytest.raises(BadLongitudeException):
            client.get_pass_times(1, 0, 1, 1)

    def test_get_pass_times_bad_altitude(self):
        client = Client()
        with pytest.raises(BadAltitudeException):
            client.get_pass_times(1, 1, 0, 1)

    def test_get_pass_times_bad_number(self):
        client = Client()
        with pytest.raises(BadNumberException):
            client.get_pass_times(1, 1, 1, 0)

    def test_get_date_of_next_pass(self):
        client = Client()
        response = client.get_date_of_next_pass()
        assert isinstance(response, datetime)
