import time

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common import TimeoutException, NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


from base.base_class import Base

class Login_page(Base):

    url = "https://www.dns-shop.ru/"
    # url_2 = "https://www.citilink.ru/?_action=login&_success_login=1"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    autorization_button = "//div[@class='user-profile__login']"
    enter_button = "//*[@id='header-search']/div/div[3]/div[2]/div/div/div[3]/div/div[2]/div/div[1]/button"
    enter_password_button = "//*[@id='modals']/div/div/div/div/div/div[4]/div[2]/div/div/div[2]"
    user_name = "//input[@class='base-ui-input-row__input base-ui-input-row__input_with-icon']"
    user_password = "/html/body/div/div/header/div[2]/div/div/div/div/div/div[3]/div/input"
    continue_button = "//*[@id='modals']/div/div/div/div/div/div[6]/div/button"
    # send_code_button = "//span[@class = 'base-ui-button-v2__text']"
    # enter_code_field = "//input[@class = 'base-ui-input-row__input']"
    # continue_button = "//button[@class = 'base-ui-button-v2_big base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2']"
    ok_moscow_button = "//*[@id='header-desktop']/div/div/div/ul/li[1]/div/div[2]/div[2]/div[1]/div/button[1]"


    # Getters

    def get_autorization_button(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.autorization_button)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.enter_button)))


    def get_enter_password_button(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.enter_password_button)))

    def get_user_name(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_password(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # def get_send_code_button(self):
    #     return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_code_button)))
    #
    # def get_enter_code_field(self):
    #     return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_code_field)))
    #
    # def get_continue_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def location_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ok_moscow_button)))




    # Actions

    def click_autorization_button(self):
        self.get_autorization_button().click()
        print("Click login button")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click login button")

    def click_enter_password_button(self):
        self.get_enter_password_button().click()
        print("Click enter password button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user_name")

    def input_user_password(self, password):
        self.get_user_password().send_keys(password)
        print("input password_name")


    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")

    # def input_code(self):
    #     rescue_code = input("Введите код из почты: ")
    #     input_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_code_field)))
    #     input_field.send_keys(rescue_code)
    #     print(f"Code Text {rescue_code}")
    #     print("input Code text")
    #
    #
    def click_moscow_button(self):
        self.location_button().click()
        print("Login button continue")


    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(3)
        self.click_moscow_button()

        time.sleep(1)
        self.click_autorization_button()
        self.click_enter_button()
        self.click_enter_password_button()
        time.sleep(1)
        self.input_user_name("kot9ira@list.ru")
        self.input_user_password("creature")
        self.click_continue_button()
        time.sleep(3)





