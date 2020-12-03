# import os
# import tempfile
# import requests
import pytest
from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse
from ..app import app as grocery 
from .. import database



# Can use werkzeug functions as a work around https://werkzeug.palletsprojects.com/en/1.0.x/test/#werkzeug.test.Client
# Client fixture isn't working need to rewrite the client fixture
# .run attribute in Flask
# As part of my fixture, import and run my app then use requests library to communicate with it 
# https://github.com/miguelgrinberg/flasky
# Mock database creation


# Pytest fixture is working. It is using app's live db to run its tests
# Need to find a way to get a flag outside of app and then pick a 'test' db in client 


@pytest.fixture
def client():
    # pick_db = database.choose_engine('test')
    return Client(grocery, BaseResponse)


def test_route_home(client):
    print(dir(client))
    resp = client.get('/')
    assert 200 == resp.status_code
    assert "Make shopping a breeze!" in str(resp.data)

# Create teardown of db pop() and teardown()