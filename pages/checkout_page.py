import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class  Checkout_page(Base):

    #Locator

    onwards_1_button = "//*[@id='bx-soa-region']/div[2]/div[3]/div/a"
    onwards_2_button = "//*[@id='bx-soa-paysystem']/div[2]/div[4]/div/a[2]"
    onwards_3_button = "//*[@id='bx-soa-delivery']/div[2]/div[3]/div/a[2]"
    name = "//input[@id='soa-property-1']"
    email = "//input[@id='soa-property-3']"
    phone = "//input[@id='soa-property-2']"
    onwards_4_button = "//*[@id='bx-soa-properties']/div[2]/div[3]/div/a[2]"
    # model_word = "//*[@id='bx-soa-basket']/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/a"
    price_word = "//*[@id='bx-soa-basket']/div[2]/div[1]/div/div/div/div[3]/div[2]/strong/span[1]"
    onwards_5_button = "//div[@id='bx-soa-orderSave']/a"

    #Getters

    def get_onwards_1_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.onwards_1_button)))

    def get_onwards_2_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.onwards_2_button)))

    def get_onwards_3_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.onwards_3_button)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_onwards_4_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.onwards_4_button)))

    # def get_model_word(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.model_word)))

    def get_price_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_word)))

    def get_onwards_5_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.onwards_5_button)))

    #Action

    def click_onwards_1_button(self):
        self.get_onwards_1_button().click()
        print("Click onwards 1 button")

    def click_onwards_2_button(self):
        self.get_onwards_2_button().click()
        print("Click onwards 2 button")

    def click_onwards_3_button(self):
        self.get_onwards_3_button().click()
        print("Click onwards 3 button")

    def input_name(self, name):
        self.get_name().send_keys(name)
        print("Input name")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Input phone")

    def click_onwards_4_button(self):
        self.get_onwards_4_button().click()
        print("Click onwards 4 button")

    def click_onwards_5_button(self):
        self.get_onwards_5_button().click()
        print("Click onwards 5 button")

    # Methods

    """Оформление заказа"""

    def formalization(self):
        self.get_current_url()
        self.click_onwards_1_button()
        time.sleep(2)
        self.click_onwards_2_button()
        time.sleep(2)
        self.click_onwards_3_button()
        time.sleep(2)
        self.input_name("")
        time.sleep(2)
        self.input_email("")
        time.sleep(2)
        self.input_phone("9111131214")
        time.sleep(2)
        self.click_onwards_4_button()
        time.sleep(2)
        # self.assert_word(self.get_model_word(), "Часы Apple Watch Series 8 GPS 45mm Midnight  Aluminum Case/Midnight Sport Band (MNUJ3)")
        # time.sleep(2)
        self.assert_word(self.get_price_word(), "37 950")
        time.sleep(2)
        self.click_onwards_5_button()
        time.sleep(2)
        self.get_screenshot()


