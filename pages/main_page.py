import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class  Main_page(Base):

    #Locator

    select_menu_smart_watch = "//nav[@id='cont_catalog_menu_rIpOz9']"
    select_smart_watch = "//*[@id='catalog-page']/div/div/div[2]/a[1]/span[1]"
    select_manufacturer = "//*[@id='marka']/div/header/span"
    select_apple = "//*[@id='marka']/div/div/label[1]/span"
    select_apply = "//button[@class='btn btn--blue btn-main show-results']"
    select_apple_watch = "//button[@id='bx_3966226736_blocks-78503_buy_link']"
    select_cart = "//div[@id='basket']"
    select_checkout = "//*[@id='popup_basket']/div[3]/div/a"

    #Getters

    def get_select_menu_smart_watch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_menu_smart_watch)))

    def get_select_smart_watch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_smart_watch)))

    def get_select_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_manufacturer)))

    def get_select_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_apple)))

    def get_select_apply(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_apply)))

    def get_select_apple_watch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_apple_watch)))

    def get_select_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cart)))

    def get_select_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_checkout)))

    #Action

    def click_select_menu_smart_watch(self):
        self.get_select_menu_smart_watch().click()
        print("Click select menu smart watch")

    def click_select_smart_watch(self):
        self.get_select_smart_watch().click()
        print("Click select smart watch")

    def click_select_manufacturer(self):
        self.get_select_manufacturer().click()
        print("Click select manufacturer")

    def click_select_apple(self):
        self.get_select_apple().click()
        print("Click select apple")

    def click_select_apply(self):
        self.get_select_apply().click()
        print("Click select apply")

    def click_select_apple_watch(self):
        self.get_select_apple_watch().click()
        print("Click select apple watch")

    def click_select_cart(self):
        self.get_select_cart().click()
        print("Click select cart")
        time.sleep(5)
        self.get_select_checkout().click()
        print("Click select checkout")

    # Methods

    """Выставление параметризированного поиска через фильтры каталога"""

    def select_product_1(self):
        with allure.step("select_product_1"):
            Logger.add_start_step(method='select_product_1')
            self.get_current_url()
            self.click_select_menu_smart_watch()
            self.click_select_smart_watch()
            self.click_select_manufacturer()
            self.click_select_apple()
            self.click_select_apply()
            time.sleep(5)
            self.click_select_apple_watch()
            time.sleep(5)
            self.click_select_cart()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='select_product_1')






