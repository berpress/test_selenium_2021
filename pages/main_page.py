from locators.main_page import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def search(self, text: str):
        element = self.input(MainPageLocators.SEARCH_INPUT, text)
        self.click_enter(element)

