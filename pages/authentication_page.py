from pages.base_page import BasePage
from pages.create_customer_account_page import CreateCustomerAccountPage
from selenium.webdriver.common.by import By

class AuthenticationPageLocators:
    EMAIL_INPUT = (By.ID, "email_create")
    CREATE_ACCOUNT_BTN = (By.ID, "SubmitCreate")

class AuthenticationPage(BasePage):
    """
    Authentication page object
    """
    def enter_email_and_click_create_account(self, email):
        """
        Enters email and goes to Registration page
        :param email:
        :return:
        """
        self.driver.find_element(*AuthenticationPageLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*AuthenticationPageLocators.CREATE_ACCOUNT_BTN).click()
        return CreateCustomerAccountPage(self.driver)

    # TODO: create bigger method
    def create_account_with_email(self, email):
        pass

    def log_in(self, email, password):
        pass