import time

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


class BuySmart(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    catalog_button = "//*[@id='catalog']/div[1]/div[3]/a/a"
    smart_button = "//a[@href='/catalog/17a8a01d16404e77/smartfony/']"
    year_button = "/html/body/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/a[4]"
    left_price_filter = "//input[@type = 'number']"
    diagonal_filter = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[15]/a/span"
    diagonal_radio_button = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[15]/div/div/div[3]/label[6]/span"
    diagonal_button_check = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/button[1]"
    buy_xiaomi_rn12pro = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[4]/div[9]/div[4]/button[2]"
    xiaomi_price = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[4]/div[9]/div[4]/div/div[1]"


    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_smart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smart_button)))

    def get_year_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.year_button)))

    def get_left_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.left_price_filter)))

    def get_diagonal_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.diagonal_filter)))

    def get_diagonal_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.diagonal_radio_button)))

    def get_diagonal_filter_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.diagonal_button_check)))

    def get_buy_xiaomi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_xiaomi_rn12pro)))

    def get_xiaomi_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xiaomi_price)))


    # Actions

    def move_catalog_button(self):
        action = ActionChains(self.driver)
        catalog_button_1 = self.get_catalog_button()
        action.move_to_element(catalog_button_1).perform()
        print("Go catalog")

    def click_smart_button(self):
        self.get_smart_button().click()
        print("Go smart")

    def click_year_button(self):
        self.get_year_button().click()
        print("Go year")

    def get_filter_price(self):
        self.scroll_window(700)
        filter_low = self.get_left_price_filter()
        time.sleep(1)
        filter_low.send_keys("25000")
        print("Go low price")


    def click_scroll_element(self):
        self.scroll_window(1600)
        time.sleep(2)
        self.get_diagonal_filter().click()
        time.sleep(1)
        print("Go filter")


    def click_diagonal_checkbox(self):
        self.get_diagonal_radio_button().click()
        print("Go filter radiobutton")

    def click_diagonal_filter_continue(self):
        self.get_diagonal_filter_continue().click()
        print("Go filter continue")

    def check_xiaomi_price(self):
        smart_page_price = self.get_xiaomi_price()
        text_price = smart_page_price.text
        print(text_price)

    def buy_xiaomi(self):
        self.scroll_window(4000)
        time.sleep(1)
        self.get_buy_xiaomi().click()
        print("Buy model!")
        time.sleep(2)
        self.get_buy_xiaomi().click()
        print("GO checkout")




    # Methods

    def buy_product(self):
        self.get_current_url()
        time.sleep(3)
        self.move_catalog_button()
        self.click_smart_button()
        self.click_year_button()
        time.sleep(2)
        self.get_filter_price()
        time.sleep(1)
        self.click_scroll_element()
        self.click_diagonal_checkbox()
        self.click_diagonal_filter_continue()
        time.sleep(1)
        self.check_xiaomi_price()
        self.buy_xiaomi()
        time.sleep(1)
        self.assert_url("https://www.dns-shop.ru/cart/")


