from selenium import webdriver
from selenium.webdriver.common.by import By

from sources_.basePage import BasePage

from common_.utilities_ import customLogger


class UserReportArea(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the UserReportArea class.
        """
        super().__init__(driver)

        self.__contactAreaLocator = (By.CSS_SELECTOR, ".contact")

        self.__nameFieldLocator = (By.CSS_SELECTOR, "[data-testid='ContactName']")
        self.__emailFieldLocator = (By.CSS_SELECTOR, "[data-testid='ContactEmail']")
        self.__phoneFieldLocator = (By.CSS_SELECTOR, "[data-testid='ContactPhone']")
        self.__subjectFieldLocator = (By.CSS_SELECTOR, "[data-testid='ContactSubject']")
        self.__messageFieldLocator = (By.CSS_SELECTOR, "[data-testid='ContactDescription']")
        self.__submitButtonLocator = (By.ID, "submitContact")
        self.__userReportConfirmMessageLocator = (By.XPATH, "(//div[@class='row contact']/div)[2]")
        self.__validationAlertLocator = (By.CSS_SELECTOR, ".alert-danger")

    def __validation_messages_check(self, expectedMessages):
        """
            Checks the expected validation message presence and correctness.
        """
        validationMessagesElement = self._find_element(self.__validationAlertLocator)
        validationMessages = self._get_element_text(validationMessagesElement).split("\n")
        for message in expectedMessages.values():
            if message in validationMessages:
                return True
        else:
            customLogger.logger("WARNING", "The expected validation message is missing")
            return False

    def fill_contact_form_name_field(self, name):
        """
            Fills the contact form name field with provided name.
        """
        nameFieldElement = self._find_element(self.__nameFieldLocator)
        self._fill_field(nameFieldElement, name)

    def fill_contact_form_email_field(self, email):
        """
            Fills the contact form Email field with provided Email.
        """
        emailFieldElement = self._find_element(self.__emailFieldLocator)
        self._fill_field(emailFieldElement, email)

    def fill_contact_form_phone_field(self, phoneNumber):
        """
            Fills the contact form phone field with provided phone number.
        """
        phoneFieldElement = self._find_element(self.__phoneFieldLocator)
        self._fill_field(phoneFieldElement, phoneNumber)

    def fill_contact_form_subject_field(self, subject):
        """
            Fills the contact form subject field with provided text.
        """
        subjectFieldElement = self._find_element(self.__subjectFieldLocator)
        self._fill_field(subjectFieldElement, subject)

    def fill_contact_form_message_field(self, message):
        """
            Fills the contact form message field with provided text.
        """
        messageFieldElement = self._find_element(self.__messageFieldLocator)
        self._fill_field(messageFieldElement, message)

    def click_to_submit_button(self):
        """
            Clicks to the contact form Submit button
        """
        submitButtonElement = self._find_element(self.__submitButtonLocator)
        self._click_to_element(submitButtonElement)

    def is_report_confirmation_message_correct(self, name, subject):
        """
            Check if the user report confirmation message is present and name and subject are correctly inserted into it.
        """
        confirmationMessageElement = self._find_element(self.__userReportConfirmMessageLocator)
        confirmationMessageText = self._get_element_text(confirmationMessageElement).split("\n")
        for text in confirmationMessageText:
            if name in text:
                continue
            if subject in text:
                return True
        else:
            customLogger.logger("WARNING", "The provided name and subject are not found in message")
            return False

    def is_validation_alert_message_present(self):
        """
            Checks the validation messages presence
        """
        return self._is_element_present(self.__validationAlertLocator)

    def is_name_validation_message_correct(self):
        """
            Checks the Name field validation message correctness.
        """
        from testData_.data import nameValidationMessages
        try:
            return self.__validation_messages_check(nameValidationMessages)
        except:
            customLogger.logger("WARNING", "The name validation message is incorrect or missing")

    def is_email_validation_message_correct(self):
        """
            Checks the Email field validation message correctness
        """
        from testData_.data import emailValidationMessages
        try:
            return self.__validation_messages_check(emailValidationMessages)
        except:
            customLogger.logger("WARNING", "The Email validation message is incorrect or missing")

    def is_phone_number_validation_message_correct(self):
        """
            Checks the Phone number field validation message correctness
        """
        from testData_.data import phoneValidationMessages
        try:
            return self.__validation_messages_check(phoneValidationMessages)
        except:
            customLogger.logger("WARNING", "The phone number validation message is incorrect or missing")

    def is_subject_validation_message_correct(self):
        """
            Checks the Subject field validation message correctness
        """
        from testData_.data import subjectValidationMessages
        try:
            return self.__validation_messages_check(subjectValidationMessages)
        except:
            customLogger.logger("WARNING", "The subject validation message is incorrect or missing")

    def is_message_validation_message_correct(self):
        """
            Checks the Message field validation message correctness
        """
        from testData_.data import messageValidationMessages
        try:
            return self.__validation_messages_check(messageValidationMessages)
        except:
            customLogger.logger("WARNING", "The message validation message is incorrect or missing")
