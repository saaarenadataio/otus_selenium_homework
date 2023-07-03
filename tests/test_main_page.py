from page_objects.main_page import Main_Page


def test_check_empty_shopping_card_label(driver):
    Main_Page(driver).check_empty_shopping_card_label()


def test_change_currency(driver):
    Main_Page(driver).change_currency("$ US Dollar")
