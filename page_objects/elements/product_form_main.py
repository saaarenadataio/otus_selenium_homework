from ..basis_page import Basis_Page
from selenium.webdriver.common.by import By


from form_filler import get_random_string


class Product_Form_Main(Basis_Page):
    SELF = (By.CSS_SELECTOR, "tab-general")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "div.note-editable")
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    META_TAG_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "#input-meta-description1")
    META_TAG_KEYWORD_INPUT = (By.CSS_SELECTOR, "#input-meta-keyword1")
    PRODUCT_TAGS_INPUT = (By.CSS_SELECTOR, "#input-tag1")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def fill_all_fields(self, product_name="ProductName1"):
        self._send_keys(self.PRODUCT_NAME_INPUT, product_name)
        self._send_keys(self.DESCRIPTION_INPUT, get_random_string())
        self._send_keys(self.META_TAG_TITLE_INPUT, get_random_string())
        self._send_keys(self.META_TAG_DESCRIPTION_INPUT, get_random_string())
        self._send_keys(self.META_TAG_KEYWORD_INPUT, get_random_string())
        self._send_keys(self.PRODUCT_TAGS_INPUT, get_random_string())

    def submit_form(self):
        self.fill_in_all_fields()
        self.element(self.SUBMIT_BUTTON).click()
