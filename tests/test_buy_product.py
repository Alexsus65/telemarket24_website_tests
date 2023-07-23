import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.cancel_page import Cancel_page
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.login_page import Login_page
from pages.main_page import Main_page

"""Smoke-тест интернет магазина ТЕЛЕМАРКЕТ24"""

@allure.description("Test buy product 1")
def test_buy_product_1(set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-notifications")
    patch = 'C:\\Users\\admin\\PycharmProjects\\resource\\chromedriver.exe'
    s = Service(patch)
    driver = webdriver.Chrome(options=options, service=s)

    print("Start Test 1")

    """Авторизация на сайте"""

    login = Login_page(driver)
    login.authorization()

    """Выставление параметризированного поиска через фильтры каталога"""

    search = Main_page(driver)
    search.select_product_1()

    """Подтверждение заказа в корзине"""

    cart = Cart_page(driver)
    cart.product_confirmation()

    """Оформление заказа"""

    checkout = Checkout_page(driver)
    checkout.formalization()

    """Отмена заказа"""

    delete = Cancel_page(driver)
    delete.deleting_order()

    print("Finish test 1")
    driver.quit()


