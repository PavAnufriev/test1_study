



class Base():
    def __init__(self, driver):
        self.driver = driver


    """ Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)


    """ Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")


    """ Method assert word"""

    def assert_word(self, result, word):
        value_word = word.text
        assert result == value_word
        print("Good value word")


    """Method scroll to element"""

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        print("Element is correct")



    """Method scroll window"""

    def scroll_window(self, scroll):
        self.driver.execute_script(f"window.scrollBy(0, {scroll});")
        print("Scroll window")












