from page_objects.card_page import Card_Page


def test_product_card_page(driver):
    Card_Page(driver).check_elements_on_page()


def test_small_radio_button(driver):
    Card_Page(driver).check_small_radio()
