from pages.base_page import BasePage
from pages.authentication_page import AuthenticationPage
from selenium.webdriver.common.by import By

class HomePageLocators:
    SIGN_IN_LINK = (By.CLASS_NAME, "login")

class HomePage(BasePage):
    """
    Landing Page object
    """
    def click_sign_in(self):
        """
        Clicks SignIn link and returns AuthenticationPage instance
        """
        # Odszukaj element
        el = self.driver.find_element(*HomePageLocators.SIGN_IN_LINK)
        # Kliknąć w ten element
        el.click()
        # Zwróć nową stronę
        return AuthenticationPage(self.driver)