from tests_.baseTest import BaseTest

from sources_.pages_.homePage_.homePage import HomePage
from sources_.pages_.homePage_.bookingArea import BookingArea


class ContentCorrectnessTests(BaseTest):
    def test_checking_header_banner_presence(self):
        """
            Test Case: Verify the presence of the banner in the page header.
        """
        # Assertions
        homePageObj = HomePage(self.driver)
        self.assertTrue(homePageObj.is_header_banner_present(), "Error: The header banner is missing")

    def test_page_description_correctness(self):
        """
            Test Case: Verify the page description correctness.
        """
        # Assertion
        homePageObj = HomePage(self.driver)
        self.assertTrue(homePageObj.is_page_description_correct(), "Error: The page description is incorrect or missing")

    def test_booking_area_title_correctness(self):
        """
            Test Case: Verify the booking area title correctness.
        """
        # Assertion
        bookingAreaObj = BookingArea(self.driver)
        self.assertTrue(bookingAreaObj.is_booking_area_title_correct(), "Error: The booking area title is incorrect or missing")
