from ..basis_page import Basis_Page
from selenium.webdriver.common.by import By


class List_Element(Basis_Page):
    SELF = (By.CSS_SELECTOR, "ul")
    ITEMS = (By.CSS_SELECTOR, "li")

    def find_item_by_text(self, text):
        items = self.element(self.SELF).find_elements(*self.ITEMS)
        item_to_change = list(filter(lambda x: x.text == text, items))[0]
        return item_to_change

    def click_item(self, text):
        item = self.find_item_by_text(text)
        item.click()
