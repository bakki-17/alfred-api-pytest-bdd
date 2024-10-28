import pytest
from utils.APIClient import APIClient
from utils.logger import logger
from utils.general_assertion import assert_status_code, assert_response_contains
import logging

# Setup logging of the process
loggers = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Instantiate the APIClient
api_client = APIClient()

def test_get_product():
    response = api_client.request('GET', 'product', '/01J9ZP372WMJ4SN8YAKS1TK0EX')

    #Log the details
    logger.info("Response status code: %s", response.status_code)
    logger.info("Response data: %s", response.json())

    #Assertions
    assert_status_code(response, 200)

    # Verify the response is a dictionary
    json_response = response.json()
    assert isinstance(json_response, dict), 'Response is not a dictionary'

def test_get_all_products():
    response = api_client.request('GET', 'product', '/01J9ZP372WMJ4SN8YAKS1TK0EX/related')

    #Log the details
    logger.info("Response status code: %s", response.status_code)
    logger.info("Response data: %s", response.json())

    #Assertions
    assert_status_code(response, 200)

# def test_get_product_data():
#     response = api_client.request('GET', 'product', '/01J9ZP372WMJ4SN8YAKS1TK0EX')

#     json_response = response.json()

#     assert_response_contains()