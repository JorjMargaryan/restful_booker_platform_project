import unittest

from tests_.testCases_.contentCorrectnessTests_.contentCorrectnessTests import ContentCorrectnessTests
from tests_.testCases_.bookingCreationTests_.bookingCreationTests import BookingCreationTests
from tests_.testCases_.communicationWithSupportTests_.userReportTests import UserReportTests
from tests_.testCases_.apiTests_.authenticationApiTests import AuthenticationApiTests


class TestSuites:
    """
        This class provides methods to create test suites for various testing scenarios, allowing for organized and
        purpose-driven test case grouping.
    """
    def get_regression_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(ContentCorrectnessTests("test_checking_header_banner_presence"))
        suite.addTest(ContentCorrectnessTests("test_page_description_correctness"))
        suite.addTest(ContentCorrectnessTests("test_booking_area_title_correctness"))
        suite.addTest(BookingCreationTests("test_booking_creation_functionality_with_valid_data"))
        suite.addTest(BookingCreationTests("test_booking_creation_functionality_with_invalid_data"))
        suite.addTest(UserReportTests("test_user_reporting_functionality_with_valid_data"))
        suite.addTest(UserReportTests("test_user_reporting_functionality_with_invalid_data"))
        suite.addTest(AuthenticationApiTests("test_login_endpoint_request_with_valid_data"))
        suite.addTest(AuthenticationApiTests("test_login_endpoint_request_with_invalid_data"))
        suite.addTest(AuthenticationApiTests("test_logout_endpoint_request_with_valid_data"))
        suite.addTest(AuthenticationApiTests("test_logout_endpoint_request_with_invalid_data"))
        suite.addTest(AuthenticationApiTests("test_validate_endpoint_request_with_valid_data"))
        suite.addTest(AuthenticationApiTests("test_validate_endpoint_request_with_invalid_data"))

        return suite

    def get_smoke_suite(self):
        pass

    def get_performance_suite(self):
        pass

    def get_random_suite(self):
        pass
