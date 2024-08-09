import unittest

from sources_.apiEndpointsHandler_.apiEndpointsHandler import ApiEndpointsHandler
from testData_.data import adminUserData


class AuthenticationApiTests(unittest.TestCase):
    def test_login_endpoint_request_with_valid_data(self):
        apiEndpointsHandlerObj = ApiEndpointsHandler()
        responseStatus = apiEndpointsHandlerObj.request_to_login_endpoint(adminUserData.username, adminUserData.password)
        assert responseStatus == 200, f"Error: Login request with valid data failed with status code{responseStatus}"

    def test_login_endpoint_request_with_invalid_data(self):
        apiEndpointsHandlerObj = ApiEndpointsHandler()
        responseStatus = apiEndpointsHandlerObj.request_to_login_endpoint("invalid", "invalid")
        assert responseStatus == 403, f"Error: Login request with invalid data failed with status code{responseStatus}"

    def test_logout_endpoint_request_with_valid_data(self):
        apiEndpointsHandlerObj = ApiEndpointsHandler()
        loginResponseHeaders = apiEndpointsHandlerObj.get_response_headers_from_login_endpoint(adminUserData.username, adminUserData.password)
        token = apiEndpointsHandlerObj.extract_token_from_headers(loginResponseHeaders)
        responseStatus = apiEndpointsHandlerObj.request_to_logout_endpoint(token)
        assert responseStatus == 200, f"Error: Logout request with valid data failed with status code{responseStatus}"

    def test_logout_endpoint_request_with_invalid_data(self):
        apiEndpointsHandlerObj = ApiEndpointsHandler()
        responseStatus = apiEndpointsHandlerObj.request_to_logout_endpoint("invalidToken")
        assert responseStatus == 403, f"Error: Logout request with invalid data failed with status code{responseStatus}"

    def test_validate_endpoint_request_with_valid_data(self):
        apiEndpointsHandlerObj = ApiEndpointsHandler()
        loginResponseHeaders = apiEndpointsHandlerObj.get_response_headers_from_login_endpoint(adminUserData.username, adminUserData.password)
        token = apiEndpointsHandlerObj.extract_token_from_headers(loginResponseHeaders)
        responseStatus = apiEndpointsHandlerObj.request_to_validate_endpoint(token)
        assert responseStatus == 200, f"Error: Validate request with valid data failed with status code{responseStatus}"

    def test_validate_endpoint_request_with_invalid_data(self):
        apiEndpointsHandlerObj = ApiEndpointsHandler()
        responseStatus = apiEndpointsHandlerObj.request_to_validate_endpoint("invalidToken")
        assert responseStatus == 403, f"Error: Validate request with invalid data failed with status code{responseStatus}"
