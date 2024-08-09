from tests_.baseTest import BaseTest

from sources_.pages_.homePage_.userReportArea import UserReportArea
from scripts_.generateFakeData import GenerateFakeData

from testData_.data import invalidEmail, invalidPhoneNumber


class UserReportTests(BaseTest):
    def test_user_reporting_functionality_with_valid_data(self):
        """
            Test Case: Verify the functionality of the user reporting with valid data.
        """
        # Act
        userReportAreaObj = UserReportArea(self.driver)
        generateFakeData = GenerateFakeData()
        name = generateFakeData.generate_first_name() + generateFakeData.generate_last_name()
        userReportAreaObj.fill_contact_form_name_field(name)
        email = generateFakeData.generate_gmail()
        userReportAreaObj.fill_contact_form_email_field(email)
        phoneNumber = generateFakeData.generate_armenian_phone_number()
        userReportAreaObj.fill_contact_form_phone_field(phoneNumber)
        subject = generateFakeData.generate_subject()
        userReportAreaObj.fill_contact_form_subject_field(subject)
        message = generateFakeData.generate_message()
        userReportAreaObj.fill_contact_form_message_field(message)
        userReportAreaObj.click_to_submit_button()

        # Assertion
        self.assertFalse(userReportAreaObj.is_validation_alert_message_present(), "Error: The user report is failed")
        self.assertTrue(userReportAreaObj.is_report_confirmation_message_correct(name, subject), "Error: The confirmation message is incorrect or missing")

    def test_user_reporting_functionality_with_invalid_data(self):
        """
            Test Case: Verify that user reporting functionality has checks for incorrect data.
        """
        # Act
        userReportAreaObj = UserReportArea(self.driver)
        generateFakeData = GenerateFakeData()
        name = ""
        userReportAreaObj.fill_contact_form_name_field(name)
        email = invalidEmail
        userReportAreaObj.fill_contact_form_email_field(email)
        phoneNumber = invalidPhoneNumber
        userReportAreaObj.fill_contact_form_phone_field(phoneNumber)
        subject = ""
        userReportAreaObj.fill_contact_form_subject_field(subject)
        message = ""
        userReportAreaObj.fill_contact_form_message_field(message)
        userReportAreaObj.click_to_submit_button()

        # Assertion
        self.assertTrue(userReportAreaObj.is_validation_alert_message_present(), "Error: The validation messages are missing")
        self.assertTrue(userReportAreaObj.is_name_validation_message_correct(), "Error: The Name validation message is incorrect or missing")
        self.assertTrue(userReportAreaObj.is_email_validation_message_correct(), "Error: The Email validation message is incorrect or missing")
        self.assertTrue(userReportAreaObj.is_phone_number_validation_message_correct(), "Error: The phone number validation message is incorrect or missing")
        self.assertTrue(userReportAreaObj.is_subject_validation_message_correct(), "Error: The subject validation message is incorrect or missing")
        self.assertTrue(userReportAreaObj.is_message_validation_message_correct(), "Error: The message validation message is incorrect or missing")


