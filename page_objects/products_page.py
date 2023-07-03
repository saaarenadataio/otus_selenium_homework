from page_objects.basis_page import Basis_Page
from page_objects.elements.product_form_main import Product_Form_Main
from page_objects.elements.product_form_data import Product_Form_Data
from page_objects.elements.filter_form import Filter_Form
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class Products_Page(Basis_Page):
    CREATE_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    COPY_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Copy']")
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
    NAV_TAB_GENERAL = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(1) > a")
    NAV_TAB_DATA = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a")
    PRODUCT_FORM = (By.CSS_SELECTOR, "#form-product")
    SELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, "input[type=checkbox]")

    def click_add_new_product_button(self):
        self.element(self.CREATE_NEW_PRODUCT_BUTTON).click()

    def click_save_product_button(self):
        self.element(self.SAVE_PRODUCT_BUTTON).click()

    def click_nav_tab_data(self):
        self.element(self.NAV_TAB_DATA).click()

    def check_success_message(self):
        return (
            self.element(self.SUCCESS_MESSAGE).text
            == "Success: You have modified products!"
        )

    def create_new_product(self, product_name="ProductName1"):
        self.click_add_new_product_button()
        Product_Form_Main(self.driver).fill_all_fields(product_name)
        self.click_nav_tab_data()
        Product_Form_Data(self.driver).fill_in_all_fields()
        self.click_save_product_button()
        self.check_success_message()

    def delete_product(self, product_name):
        Filter_Form(self.driver).filter_product_by_name(product_name)
        self.element(self.SELECT_ALL_CHECKBOX).click()
        self.element(self.DELETE_PRODUCT_BUTTON).click()
        Alert(self.driver).accept()
        self.check_success_message()
