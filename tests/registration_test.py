from tests.base_test import BaseTest
from test_data.registration_data import RegistrationData
import test_data.registration_data
from ddt import data, unpack, ddt
from utils.gender import Gender
from time import sleep
import os


@ddt
class RegistrationTest(BaseTest):
    """
    Registration tests
    """
    def setUp(self):
        super().setUp()
        self.test_data = RegistrationData()

    def test_no_first_name_entered(self):
        """
        TC 001: User does not enter his first name
        """
        # KROKI
        # 1. Kliknij "Sign In"
        self.authentication_page = self.home_page.click_sign_in()
        # 2. Wpisz email
        # 3. Kliknij przycisk "Create account"
        self.create_customer_account_page = self.authentication_page.enter_email_and_click_create_account(self.test_data.registration_email)
        # 4. Wybierz płeć
        self.create_customer_account_page.choose_gender(self.test_data.registration_gender)
        # 5. Wpisz nazwisko
        self.create_customer_account_page.enter_last_name(self.test_data.registration_last_name)
        # 6. Sprawdź, czy email wpisany wcześniej wyświetla się polu email
        self.assertEqual(self.test_data.registration_email, self.create_customer_account_page.get_email())
        # 7. Wpisz hasło
        self.create_customer_account_page.enter_password(self.test_data.password)
        # 8. Wybierz datę urodzenia
        self.create_customer_account_page.select_birthdate(self.test_data.day_of_birth,
                                                           self.test_data.month_of_birth,
                                                           self.test_data.year_of_birth)
        # 9. Kliknij "Register"
        self.create_customer_account_page.click_register_btn()
        # Sprawdź poprawność komunikatu o liczbie błędów
        self.assertEqual("There is 1 error", self.create_customer_account_page.get_number_of_user_errors_message())
        # Sprawdź poprawność komunikatu o niewpisaniu imienia
        self.assertEqual('firstname is required.', self.create_customer_account_page.get_user_error_messages()[0])
        sleep(3)

    @data(*test_data.registration_data.get_csv_data("../test_data/registration.csv"))
    @unpack
    def test_no_first_name_ddt(self, gender,first_name,last_name,email,password,day,month,year):
        # 1. Kliknij "Sign In"
        self.authentication_page = self.home_page.click_sign_in()
        # 2. Wpisz email
        # 3. Kliknij przycisk "Create account"
        self.create_customer_account_page = self.authentication_page.enter_email_and_click_create_account(email)
        # 4. Wybierz płeć
        if gender == "male":
            self.create_customer_account_page.choose_gender(Gender.MALE)
        else:
            self.create_customer_account_page.choose_gender(Gender.FEMALE)
        # 5. Wpisz nazwisko
        self.create_customer_account_page.enter_last_name(last_name)
        # 6. Sprawdź, czy email wpisany wcześniej wyświetla się polu email
        self.assertEqual(email, self.create_customer_account_page.get_email())
        # 7. Wpisz hasło
        self.create_customer_account_page.enter_password(password)
        # 8. Wybierz datę urodzenia
        self.create_customer_account_page.select_birthdate(day,
                                                           month,
                                                           year)
        # 9. Kliknij "Register"
        self.create_customer_account_page.click_register_btn()
        # Sprawdź poprawność komunikatu o liczbie błędów
        self.assertEqual("There is 1 error", self.create_customer_account_page.get_number_of_user_errors_message())
        # Sprawdź poprawność komunikatu o niewpisaniu imienia
        self.assertEqual('firstname is required.', self.create_customer_account_page.get_user_error_messages()[0])
        sleep(3)


# def test_no_first_and_last_name_entered(self):
    #     """
    #     TC 002: User does not enter his first and last name
    #     """
    #     # KROKI
    #     # 1. Kliknij "Sign In"
    #     self.authentication_page = self.home_page.click_sign_in()
    #     # 2. Wpisz email
    #     # 3. Kliknij przycisk "Create account"
    #     self.create_customer_account_page = self.authentication_page.enter_email_and_click_create_account("hdgsfhg@pw.pl")
    #     # 4. Wybierz płeć
    #     self.create_customer_account_page.choose_gender(Gender.FEMALE)