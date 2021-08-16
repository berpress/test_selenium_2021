from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

BASE_URL = "http://www.python.org"


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def open_main_page(self):
        self.driver.get(BASE_URL)

    def get_title(self) -> str:
        return self.driver.title

    def search(self, text: str):
        element = self.driver.find_element_by_name("q")
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)

    def get_page_source(self) -> str:
        return self.driver.page_source

    def quit(self):
        self.driver.quit()
