import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class  Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locator

    # model_word = "//span[@data-entity='basket-item-nam']"
    # price_word = "//span[@id='basket-item-price-1455039'"
    checkout_button = "//button[@class='btn btn--blue btn btn-lg btn-default basket-btn-checkout']"

    #Getters

    # def get_model_word(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.model_word)))

    # def get_price_word(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_word)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

     #Action

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods

    def product_confirmation(self):
        self.get_current_url()
        # self.assert_word(self.get_model_word(), "Часы Apple Watch Series 8 GPS 45mm Midnight  Aluminum Case/Midnight Sport Band (MNUJ3)")
        # time.sleep(1)
        # self.assert_word(self.get_price_word(), "38 458 ₽")
        # time.sleep(1)
        self.click_checkout_button()







