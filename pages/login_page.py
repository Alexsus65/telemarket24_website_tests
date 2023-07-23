import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class Login_page(Base):

    url = 'https://telemarket24.ru/'

    #Locator

    account_menu = "//div[@id='account-menu-toggler']"
    inlet = "//*[@id='account-menu-toggler']/span/span/a"
    email = "//input[@name='USER_LOGIN']"
    password = "//input[@name='USER_PASSWORD']"
    login = "//button[@class='btn-submit btn-main']"
    profile_word = "//*[@id='account-menu-toggler']/span/span/div/ul/li[2]/a/span"

    #Getters

    def get_account_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_menu)))

    def get_inlet(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.inlet)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_profile_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_word)))

     #Action

    def click_account_menu(self):
        self.get_account_menu().click()
        print("Click account menu")

    def click_inlet(self):
        self.get_inlet().click()
        print("Click inlet")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login(self):
        self.get_login().click()
        print("Click login")

     # Methods

    """Авторизация на сайте"""

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_account_menu()
            self.click_inlet()
            self.input_email("igsergeev@inbox.ru")
            self.input_password("********")
            self.click_login()
            self.click_account_menu()
            self.assert_word(self.get_profile_word(), "Мой кабинет")
            Logger.add_end_step(url=self.driver.current_url, method='authorization')









