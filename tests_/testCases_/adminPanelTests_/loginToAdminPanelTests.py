from tests_.baseTest import BaseTest

from sources_.pages_.homePage_.homePage import HomePage
from sources_.pages_.adminPanelPage import AdminPanelPage
from testData_.data import adminUserData


class LoginToAdminPanelTests(BaseTest):
    def test_login_with_valid_data(self):
        """
            Test Case: Verify the functionality of the login to admin dashboard with valid data.
        """
        # Act
        homePageObj = HomePage(self.driver)
        homePageObj.click_to_admin_panel_button()
        adminPanelPageObj = AdminPanelPage(self.driver)
        adminPanelPageObj.fill_username_field(adminUserData.username)
        adminPanelPageObj.fill_password_field(adminUserData.password)
        adminPanelPageObj.click_to_login_button()

        # Assertion
        self.assertTrue(adminPanelPageObj.is_user_logged_in(), "Error: The user is not logged in")

    def test_login_with_invalid_data(self):
        """
            Test Case: Verify the functionality of the login to admin dashboard with invalid data.
        """
        # Act
        homePageObj = HomePage(self.driver)
        homePageObj.click_to_admin_panel_button()
        adminPanelPageObj = AdminPanelPage(self.driver)
        adminPanelPageObj.fill_username_field("invalid")
        adminPanelPageObj.fill_password_field("invalid")
        adminPanelPageObj.click_to_login_button()

        # Assertion
        self.assertTrue(adminPanelPageObj.is_invalid_login_data_validation_works(), "Error: There is no validation for invalid login data")
