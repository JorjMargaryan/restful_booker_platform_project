from selenium import webdriver
from selenium.webdriver.common.by import By

from sources_.basePage import BasePage

from common_.utilities_ import customLogger


class AdminPanelPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the AdminPanelPage class.
        """
        super().__init__(driver)
        self.__userNameFieldLocator = (By.CSS_SELECTOR, "[data-testid='username']")
        self.__passwordFieldLocator = (By.CSS_SELECTOR, "[data-testid='password']")
        self.__loginButtonLocator = (By.CSS_SELECTOR, "[data-testid='submit']")

        self.__navigationMenuButtonsLocator = (By.CSS_SELECTOR, ".nav-link")



    def fill_username_field(self, userName):
        """
            Fills the username field with provided username.
        """
        userNameFieldElement = self._find_element(self.__userNameFieldLocator)
        self._fill_field(userNameFieldElement, userName)

    def fill_password_field(self, password):
        """
            Fills password field with provided password.
        """
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_to_login_button(self):
        """
            Clicks to the Login button.
        """
        loginButtonElement = self._find_element(self.__loginButtonLocator)
        self._click_to_element(loginButtonElement)

    def quick_login(self, userName, password):
        """
            Makes login actions in one method for quickly login.
        """
        self.fill_username_field(userName)
        self.fill_password_field(password)
        self.click_to_login_button()

    def is_user_logged_in(self):
        """
            Checks whether the user is logged in.
        """
        try:
            self._find_element(self.__navigationMenuButtonsLocator)
            return True
        except:
            customLogger.logger("WARNING", "Navigation menu buttons are missing, the user is not logged in")
            return False

    def is_invalid_login_data_validation_works(self):
        # Capture and print console errors
        logs = self.driver.get_log('browser')

        for log in logs:
            if log['level'] == 'SEVERE':  # Only capture severe errors (e.g., 403, 500)
                customLogger.logger("WARNING", f"Console Error: {log['message']}")
                return True
            else:
                customLogger.logger("WARNING", "Invalid login data validation failed")
                return False
