from ..basis_page import Basis_Page
from selenium.webdriver.common.by import By


from form_filler import get_random_string


class Product_Form_Data(Basis_Page):
    SELF = (By.CSS_SELECTOR, "tab-data")
    PRODUCT_MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")

    def fill_in_all_fields(self):
        self._send_keys(self.PRODUCT_MODEL_INPUT, get_random_string())
