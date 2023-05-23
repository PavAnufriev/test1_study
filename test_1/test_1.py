import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.checkout_page import Checkout
from pages.login_page import Login_page
from pages.check_smart_page import BuySmart


def test_smoke_1():
    options = Options()
    options.add_argument('--disable-extensions')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path='C:\\Users\\KoT9I\\PycharmProjects\\resource\\chromedriver.exe', options=options)

    print("Start test_1")

    login = Login_page(driver)
    login.authorization()

    buy_product = BuySmart(driver)
    buy_product.buy_product()

    checkout_product = Checkout(driver)
    checkout_product.chekout()


    print("finish test")
    time.sleep(10)
    driver.quit()









