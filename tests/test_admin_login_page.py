from page_objects.admin_login_page import Admin_Login_Page


def test_admin_login_page(driver):
    Admin_Login_Page(driver).check_elements_on_page()
