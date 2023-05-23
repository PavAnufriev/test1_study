import time
from pages.check_smart_page import BuySmart

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common import TimeoutException, NoAlertPresentException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from base.base_class import Base



class Checkout(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    check_price = "//span[@class = 'price__current']"
    button_checkout = "//button[@class = 'base-ui-button-v2_medium base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2 buy-button']"
    redio_button = "#total-amount > div.total-amount__content > div.total-amount__profit-wrapper > div > div > label > span.base-ui-toggle__icon"

    # Getters


    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.check_price)))

    def button_check_out(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    def get_radio_button(self):
        radio_button_css = "#total-amount > div.total-amount__content > div.total-amount__profit-wrapper > div > div > label > span.base-ui-toggle__icon"
        return self.driver.find_element(By.CSS_SELECTOR, radio_button_css)


    # Actions

    def check_smart_price(self):
        smart_price = self.get_price()
        text_smart_price = smart_price
        print(text_smart_price)
        self.assert_word("29 999 ₽", text_smart_price)

    def click_radio_button(self):
        radio_button = self.get_radio_button()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, radio_button)))
        radio_button().click()
        print("Radio button go")

    def click_checkout_button(self):
        self.button_check_out().click()
        print("Go checkout!")


    # Methods

    def chekout(self):
        self.get_current_url()
        self.check_smart_price()
        time.sleep(2)
        # self.click_radio_button() перепробовал все возможные локаторы (
        # time.sleep(2)
        self.click_checkout_button()