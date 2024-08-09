from selenium import webdriver
from selenium.webdriver.common.by import By

from sources_.basePage import BasePage

from common_.utilities_ import customLogger


class HomePage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the HomePage class.
        """
        super().__init__(driver)
        self.__headerBannerLocator = (By.ID, "collapseBanner")
        self.__pageDescriptionLocator = (By.CSS_SELECTOR, ".hotel-description")
        self.__adminPanelButtonLocator = (By.CSS_SELECTOR, "[alt='Link to admin page']")

    def is_header_banner_present(self):
        """
           This method checks presence of the header banner.
        """
        if self._is_element_present(self.__headerBannerLocator):
            return True
        else:
            return False

    def is_page_description_correct(self):
        """
            Checks the page description presence and correctness.
        """
        from testData_.data import correctPageDescription
        from exitCodes import MessageCodes, UNEXPECTED_BEHAVIOR
        try:
            pageDescriptionElement = self._find_element(self.__pageDescriptionLocator)
            pageDescription = self._get_element_text(pageDescriptionElement)
            if pageDescription == correctPageDescription:
                return True
            else:
                customLogger.logger("WARNING", f"The description is not correct: Actual:{pageDescription}")
                return False
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} -  {str(e)}")
            exit(UNEXPECTED_BEHAVIOR)

    def click_to_admin_panel_button(self):
        """
            Clicks to the Admin panel button placed on the right side of the header banner.
        """
        adminPanelButtonElement = self._find_element(self.__adminPanelButtonLocator)
        self._click_to_element(adminPanelButtonElement)
