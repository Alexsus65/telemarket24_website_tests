import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class  Cart_page(Base):

    #Locator

    checkout_button = "//button[@class='btn btn--blue btn btn-lg btn-default basket-btn-checkout']"

    #Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

     #Action

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods

    """Подтверждение заказа в корзине"""

    def product_confirmation(self):
        with allure.step("product_confirmation"):
            Logger.add_start_step(method='product_confirmation')
            self.get_current_url()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method='product_confirmation')







