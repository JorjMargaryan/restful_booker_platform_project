from selenium import webdriver
from selenium.webdriver.common.by import By

from sources_.basePage import BasePage

from common_.utilities_ import customLogger


class BookingArea(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the BookingArea class.
        """
        super().__init__(driver)
        self.__bookingAreaTitleLocator = (By.CSS_SELECTOR, ".room-header h2")
        self.__bookThisRoomButtonLocator = (By.CSS_SELECTOR, ".openBooking")
        self.__bookFormFirstNameFieldLocator = (By.CSS_SELECTOR, ".room-firstname")
        self.__bookFormLastNameFieldLocator = (By.CSS_SELECTOR, ".room-lastname")
        self.__bookFormEmailFieldLocator = (By.CSS_SELECTOR, ".room-email")
        self.__bookFormPhoneFieldLocator = (By.CSS_SELECTOR, ".room-phone")
        self.__bookFormBookButton = (By.CSS_SELECTOR, ".btn-outline-primary.book-room")
        self.__bookFormCancelButton = (By.CSS_SELECTOR, ".btn-outline-danger.book-room")
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

    def is_booking_area_title_correct(self):
        """
            Checks the booking area title presence and correctness.
        """
        from exitCodes import MessageCodes, UNEXPECTED_BEHAVIOR
        try:
            bookingAreaTitleElement = self._find_element(self.__bookingAreaTitleLocator)
            bookingAreaTitle = self._get_element_text(bookingAreaTitleElement)
            if bookingAreaTitle[0].isupper() and bookingAreaTitle[1:].islower():
                return True
            else:
                customLogger.logger("WARNING",f"The booking area title is not correct(not capitalized). Actual:{bookingAreaTitle}")
                return False
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} -  {str(e)}")
            exit(UNEXPECTED_BEHAVIOR)

    def click_to_book_this_room_button(self):
        """
            Clicks on the 'Book this room' button.
        """
        bookThisRoomButtonElement = self._find_element(self.__bookThisRoomButtonLocator)
        self._click_to_element(bookThisRoomButtonElement)

    def fill_book_form_first_name_field(self, firstName):
        """
            Fills the book form first name field with provided name.
        """
        firstNameFieldElement = self._find_element(self.__bookFormFirstNameFieldLocator)
        self._fill_field(firstNameFieldElement, firstName)

    def fill_book_form_last_name_field(self, lastName):
        """
            Fills the book form last name field with provided name.
        """
        lastNameFieldElement = self._find_element(self.__bookFormLastNameFieldLocator)
        self._fill_field(lastNameFieldElement, lastName)

    def fill_book_form_email_field(self, email):
        """
            Fills the book form Email field with provided Email.
        """
        emailFieldElement = self._find_element(self.__bookFormEmailFieldLocator)
        self._fill_field(emailFieldElement, email)

    def fill_book_form_phone_field(self, phoneNumber):
        """
            Fills the book form phone field with provided phone number.
        """
        phoneFieldElement = self._find_element(self.__bookFormPhoneFieldLocator)
        self._fill_field(phoneFieldElement, phoneNumber)

    def click_to_book_form_book_button(self):
        """
            Clicks on the book form Book button.
        """
        bookButtonElement = self._find_element(self.__bookFormBookButton)
        self._click_to_element(bookButtonElement)

    def is_validation_alert_message_present(self):
        """
            Checks the validation messages presence
        """
        return self._is_element_present(self.__validationAlertLocator)

    def is_first_name_validation_message_correct(self):
        """
            Checks the First Name field validation message correctness
        """
        from testData_.data import firstNameValidationMessages
        try:
            return self.__validation_messages_check(firstNameValidationMessages)
        except:
            customLogger.logger("WARNING", "The first name validation message is incorrect or missing")

    def is_last_name_validation_message_correct(self):
        """
            Checks the Last Name field validation message correctness.
        """
        from testData_.data import lastNameValidationMessages
        try:
            return self.__validation_messages_check(lastNameValidationMessages)
        except:
            customLogger.logger("WARNING", "The last name validation message is incorrect or missing")

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


