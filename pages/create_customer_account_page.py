from pages.base_page import BasePage
from utils.gender import Gender
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CreateCustomerAccountPageLocators:
    GENDER_MALE = (By.ID, "id_gender1")
    GENDER_FEMALE = (By.ID, "id_gender2")
    LAST_NAME_INPUT = (By.ID, "customer_lastname")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "passwd")
    BIRTH_DAY = (By.ID, "days")
    BIRTH_MONTH = (By.ID, "months")
    BIRTH_YEAR = (By.ID, "years")
    REGISTER_BTN = (By.ID, "submitAccount")
    NUMBER_OF_USER_ERRORS_MESSAGE = (By.XPATH, '//div[@class="alert alert-danger"]/p')
    USER_ERROR_MESSAGES = (By.XPATH, '//div[@class="alert alert-danger"]/ol/li')

class CreateCustomerAccountPage(BasePage):
    def choose_gender(self, gender):
        """
        Chooses gender
        """
        if gender == Gender.FEMALE:
            self.driver.find_element(*CreateCustomerAccountPageLocators.GENDER_FEMALE).click()
        else:
            self.driver.find_element(*CreateCustomerAccountPageLocators.GENDER_MALE).click()

    def enter_last_name(self, last_name):
        """
        Enters last name
        """
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.LAST_NAME_INPUT)
        el.send_keys(last_name)

    def enter_password(self, password):
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.PASSWORD_INPUT)
        el.send_keys(password)

    def select_birthdate(self, day, month, year):
        """
        Selects user birthdate (day month and year)
        """
        # Wybór dnia
        birth_day_select = Select(self.driver.find_element(*CreateCustomerAccountPageLocators.BIRTH_DAY))
        birth_day_select.select_by_value(day)
        # Wybór miesiąca
        birth_month_select = Select(self.driver.find_element(*CreateCustomerAccountPageLocators.BIRTH_MONTH))
        birth_month_select.select_by_value(month)
        # Wybór roku
        birth_year_select = Select(self.driver.find_element(*CreateCustomerAccountPageLocators.BIRTH_YEAR))
        birth_year_select.select_by_value(year)

    def click_register_btn(self):
        self.driver.find_element(*CreateCustomerAccountPageLocators.REGISTER_BTN).click()

    def get_email(self):
        """
        Gets email visible in the Email input
        """
        # Odszukać to pole
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.EMAIL_INPUT)
        # Pobrać tekst i zwrócić go
        return el.get_attribute("value")

    def get_number_of_user_errors_message(self):
        """
        Returns message displayed to the user regarding number of errors he commited
        """
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.NUMBER_OF_USER_ERRORS_MESSAGE)
        return el.text

    def get_user_error_messages(self):
        """
        Returns list of user error messages
        """
        errors = self.driver.find_elements(*CreateCustomerAccountPageLocators.USER_ERROR_MESSAGES)
        errors_texts = []
        for e in errors:
            # Dodaję zawartość tekstową do listy
                errors_texts.append(e.text)
        return  errors_texts
