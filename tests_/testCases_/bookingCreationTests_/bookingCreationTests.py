from tests_.baseTest import BaseTest

from sources_.pages_.homePage_.bookingArea import BookingArea
from scripts_.generateFakeData import GenerateFakeData

from testData_.data import invalidEmail, invalidPhoneNumber


class BookingCreationTests(BaseTest):
    def test_booking_creation_functionality_with_valid_data(self):
        """
            Test Case: Verify the functionality of the booking creation with valid data.
        """
        # Act
        bookingAreaObj = BookingArea(self.driver)
        generateFakeData = GenerateFakeData()
        bookingAreaObj.click_to_book_this_room_button()
        firstName = generateFakeData.generate_first_name()
        bookingAreaObj.fill_book_form_first_name_field(firstName)
        lastName = generateFakeData.generate_last_name()
        bookingAreaObj.fill_book_form_last_name_field(lastName)
        email = generateFakeData.generate_gmail()
        bookingAreaObj.fill_book_form_email_field(email)
        phoneNumber = generateFakeData.generate_armenian_phone_number()
        bookingAreaObj.fill_book_form_phone_field(phoneNumber)
        bookingAreaObj.click_to_book_form_book_button()

        # Assertion
        self.assertFalse(bookingAreaObj.is_validation_alert_message_present(), "Error: The booking is failed")

    def test_booking_creation_functionality_with_invalid_data(self):
        """
            Test Case: Verify that booking functionality has checks for incorrect data.
        """
        # Act
        bookingAreaObj = BookingArea(self.driver)
        bookingAreaObj.click_to_book_this_room_button()
        firstName = ""
        bookingAreaObj.fill_book_form_first_name_field(firstName)
        lastName = ""
        bookingAreaObj.fill_book_form_last_name_field(lastName)
        email = invalidEmail
        bookingAreaObj.fill_book_form_email_field(email)
        phoneNumber = invalidPhoneNumber
        bookingAreaObj.fill_book_form_phone_field(phoneNumber)
        bookingAreaObj.click_to_book_form_book_button()

        # Assertion
        self.assertTrue(bookingAreaObj.is_validation_alert_message_present(), "Error: The validation messages are missing")
        self.assertTrue(bookingAreaObj.is_first_name_validation_message_correct(), "Error: The First Name validation message is incorrect or missing")
        self.assertTrue(bookingAreaObj.is_last_name_validation_message_correct(), "Error: The Last Name validation message is incorrect or missing")
        self.assertTrue(bookingAreaObj.is_email_validation_message_correct(), "Error: The Email validation message is incorrect or missing")
        self.assertTrue(bookingAreaObj.is_phone_number_validation_message_correct(), "Error: The phone number validation message is incorrect or missing")
