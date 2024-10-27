from pytest_bdd import given, when, then
from utils.APIClient import APIClient
from utils.logger import logger
from utils.general_assertion import assert_status_code

api_client = APIClient()

@given('the product inventory endpoint')
def step_given_product_endpoint(context):
    context.endpoint = 'products'
    # context.enpoint_path = ''

@when('sending a request to get product inventory')
def step_when_send_product_request(context):
    context.response = api_client.get(context.endpoint)
    logger.info("Response status code: %s", context.response.status_code)
    logger.info("Response data: ", context.response.json())

@then('the response contains the expected product data')
def step_then_product_retieved_successfully(context):
    assert_status_code(context.response, 200)