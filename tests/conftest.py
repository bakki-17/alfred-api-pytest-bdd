import pytest
from utils.APIClient import APIClient
import os

@pytest.fixture(scope="session")
def api_client():
    return APIClient()

# @pytest.hookimpl(trylast=True)
# def pytest_configure(config):
#     config._htmlfile = config._html.logfile


# @pytest.hookimpl(trylast=True)
# def pytest_sessionfinish(session, exitstatus):
#     file = session.config._htmlfile
#     # invoke the file opening in external tool
#     os.system('open ' + file)