import requests
from ISS import Client
import pytest
from ISS.exceptions import *
from datetime import datetime


class TestClient:

    def test_get_location(self):
        client = Client()
        response = client.get_location()
        assert isinstance(response, requests.Response)
        assert response.status_code == 200

    def test_get_pass_times(self):
        client = Client()
        response = client.get_pass_times()
        assert isinstance(response, requests.Response)
        assert response.status_code == 200

    def test_get_astronauts(self):
        client = Client()
        response = client.get_astronauts()
        assert isinstance(response, requests.Response)
        assert response.status_code == 200

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

    def test_get_next_pass_date(self):
        client = Client()
        response = client.get_next_pass_date()
        assert response is 'No passes found.' or isinstance(response, datetime)

    def test_get_number_of_astronauts(self):
        client = Client()
        response = client.get_number_of_astronauts()
        assert isinstance(response, int)

    def test_get_list_of_astronaut_names(self):
        client = Client()
        response = client.get_list_of_astronaut_names()
        assert isinstance(response, list)

    def test_get_next_pass_duration_in_seconds(self):
        client = Client()
        response = client.get_next_pass_duration_in_seconds()
        assert response is "No passes found." or isinstance(response, int)

    def test_get_set_of_occupied_spacecraft(self):
        client = Client()
        response = client.get_set_of_occupied_spacecraft()
        assert isinstance(response, set)
