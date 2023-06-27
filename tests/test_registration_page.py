from page_objects.register_page import Register_Page


def test_registration(driver):
    Register_Page(driver).check_elements_on_page()
    Register_Page(driver).register_new_user()
