from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.cancel_page import Cancel_page
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_buy_product_1(set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-notifications")
    patch = 'C:\\Users\\admin\\PycharmProjects\\resource\\chromedriver.exe'
    s = Service(patch)
    driver = webdriver.Chrome(options=options, service=s)

    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()

    search = Main_page(driver)
    search.select_product_1()

    cart = Cart_page(driver)
    cart.product_confirmation()

    checkout = Checkout_page(driver)
    checkout.formalization()

    delete = Cancel_page(driver)
    delete.deleting_order()

    print("Finish test 1")
    driver.quit()


