from page_objects.admin_main_page import Admin_Main_Page
from page_objects.admin_login_page import Admin_Login_Page
from page_objects.products_page import Products_Page

PRODUCT_NAME = "Lenovo Think Pad 2.0"


def test_product_creation(driver):
    Admin_Login_Page(driver).login_as_admin()
    Admin_Main_Page(driver).open_products_page()
    Products_Page(driver).create_new_product(PRODUCT_NAME)


def test_product_deletion(driver):
    Admin_Login_Page(driver).login_as_admin()
    Admin_Main_Page(driver).open_products_page()
    Products_Page(driver).delete_product(PRODUCT_NAME)
