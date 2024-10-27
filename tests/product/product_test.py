import pytest
from utils.APIClient import APIClient
from utils.logger import logger
from utils.general_assertion import assert_status_code
import logging

# Setup logging of the process
loggers = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Instantiate the APIClient
api_client = APIClient()

def test_get_product():
    response = api_client.request('GET', 'products')

    #Log the details
    logger.info("Response status code: %s", response.status_code)
    logger.infor("Response data: %s", response.json())

    #Assertions
    assert_status_code(response, 200)

    # Verify the response is a dictionary
    json_response = response.json()
    assert isinstance(json_response, dict), 'Response is not a dictionary'