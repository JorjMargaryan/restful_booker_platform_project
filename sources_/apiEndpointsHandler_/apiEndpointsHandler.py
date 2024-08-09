import requests

from common_.utilities_ import customLogger
from testData_.apiData import loginApiUrl, logoutApiUrl, validateApiUrl


class ApiEndpointsHandler:
    def get_response_headers_from_login_endpoint(self, userName, password):
        """
            Gets the response headers from the login endpoint after a successful request.
        """
        from exitCodes import UNEXPECTED_BEHAVIOR
        url = loginApiUrl
        headers = {'Content-Type': 'application/json'}
        payload = {'username': userName, 'password': password}
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.headers
        else:
            customLogger.logger("ERROR", f"Request failed with status code {response.status_code}.")
            exit(UNEXPECTED_BEHAVIOR)

    def request_to_login_endpoint(self, userName, password):
        """
            Checks the request to the login endpoint.
        """
        from exitCodes import UNEXPECTED_BEHAVIOR
        url = loginApiUrl
        headers = {'Content-Type': 'application/json'}
        json_data = {'username': userName, 'password': password}
        response = requests.post(url, json=json_data, headers=headers)
        return response.status_code
    def extract_token_from_headers(self, headers):
        """
            Extracts the token value from the response headers.
        """
        # Get the Set-Cookie header
        setCookieHeader = headers.get('Set-Cookie', '')
        # Extract token from Set-Cookie header
        token = None
        if setCookieHeader:
            # Split cookies by '; ' to handle multiple cookies
            cookies = setCookieHeader.split('; ')
            for cookie in cookies:
                if cookie.startswith('token='):
                    # Extract the token value
                    token = cookie[len('token='):]
                    break
        return token

    def request_to_logout_endpoint(self, token):
        """
            Checks the request to the logout endpoint.
        """
        url = logoutApiUrl
        # Prepare the headers and payload for the logout request
        headers = {'Content-Type': 'application/json'}
        payload = {'token': token}

        # Send POST request to the logout endpoint with the token in the JSON body
        response = requests.post(url, headers=headers, json=payload)

        return response.status_code


    def request_to_validate_endpoint(self, token):
        """
            Checks whether the request to the validate endpoint is successful.
        """
        url = validateApiUrl
        # Prepare the headers and payload for the logout request
        headers = {'Content-Type': 'application/json'}
        payload = {'token': token}

        # Send POST request to the logout endpoint with the token in the JSON body
        response = requests.post(url, headers=headers, json=payload)

        return response.status_code