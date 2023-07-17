import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class  Cancel_page(Base):

    #Locator

    orders = "//*[@id='mm-0']/div[2]/div[10]/table[1]/tbody/tr/td/a"
    cancel_order1 = "//*[@id='mm-0']/div[2]/main/div/div/div[2]/div[2]/div/div[4]/div[4]/a"
    cancel_order2 = "//*[@id='mm-0']/div[2]/main/div/div/div/div/form/div[3]/button/span"

    #Getters

    def get_orders(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.orders)))

    def get_cancel_order1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel_order1)))

    def get_cancel_order2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel_order2)))

    #Action

    def click_orders(self):
        self.get_orders().click()
        print("Click orders")

    def click_cancel_order1(self):
        self.get_cancel_order1().click()
        print("Click cancel order1")

    def click_cancel_order2(self):
        self.get_cancel_order2().click()
        print("Click cancel order2")

     # Methods

    """Отмена заказа"""

    def deleting_order(self):
        self.get_current_url()
        self.click_orders()
        self.click_cancel_order1()
        self.click_cancel_order2()
        self.get_screenshot()


