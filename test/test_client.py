import requests
from ISS import Client
import pytest
from ISS.exceptions import *


class TestClient:

    def test_get_location(self):
        client = Client()
        response = client.get_location()
        assert isinstance(response, requests.Response)
        assert response.status_code == 200

    def test_pass_times(self):
        client = Client()
        response = client.get_pass_times()
        assert isinstance(response, requests.Response)
        assert response.status_code == 200

    def test_astronauts(self):
        client = Client()
        response = client.get_astronauts()
        assert isinstance(response, requests.Response)
        assert response.status_code == 200

    def test_pass_times_bad_latitude(self):
        client = Client()
        with pytest.raises(BadLatitudeException):
            client.get_pass_times(0, 1, 1, 1)
