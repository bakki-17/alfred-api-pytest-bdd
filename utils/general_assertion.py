from datetime import datetime

def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, got {response.status_code}"

def assert_response_contains(response, key, expected_value):
    try: 
        json_response = response.json()
        actual_value = json_response[key]

        assert str(actual_value).strip() == str(expected_value).strip(), f"{key} is expected to be {expected_value}, got {actual_value}"

    except Exception as e:
        print(f"An error occur in comparing values for key '{key}': {e}")