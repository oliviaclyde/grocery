import os
import tempfile

import pytest

from ..app import app as grocery 

# @pytest.fixture
# def app():
#     yield grocery


@pytest.fixture
def client():
    db_fd, grocery.app.config['DATABASE'] = tempfile.mkstemp()
    grocery.app.config['TESTING'] = True

    with grocery.app.test_client() as client:
        with grocery.app.app_context():
            grocery.init_db()
        yield client 

    os.close(db_fd)
    os.unlink(grocery.app.config['DATABASE'])

