from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitTime:
    FAST = 1
    MEDIUM = 2
    SLOW = 3


class MainPage:
    LOGO = (By.CSS_SELECTOR, "#logo")
    MENU_BAR = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li.nav-item")
    SEARCH_BAR = (By.ID, "search")
    FEATURED_PRODUCT = (By.CLASS_NAME, "product-thumb")
    FOOTER = (By.XPATH, "//footer//ul")


def test_main_page_check_logo(driver):
    driver.find_element(*MainPage.LOGO)
    WebDriverWait(driver, WaitTime.FAST).until(
        EC.visibility_of_element_located(MainPage.LOGO),
        message=f"Logo of the page {MainPage.LOGO} was not loaded in {WaitTime.FAST} seconds",
    )


def test_main_check_search_bar(driver):
    menu_items = driver.find_element(*MainPage.SEARCH_BAR)
    assert menu_items, "Search bar was not found"


def test_main_page_menu_bar(driver):
    menu_items = driver.find_elements(*MainPage.MENU_BAR)
    assert (
        len(menu_items) == 8
    ), f"Wrong number of menu elements: {len(menu_items)}, expected 8"


def test_main_page_fetured_items(driver):
    fetured_items = driver.find_elements(*MainPage.FEATURED_PRODUCT)
    assert (
        len(fetured_items) == 4
    ), f"wrong number of products in 'featured' block: {len(fetured_items)} expected 4"


def test_main_page_footer_blocks(driver):
    footer_blocks = driver.find_elements(*MainPage.FOOTER)
    assert (
        len(footer_blocks) == 4
    ), f"Wrong links' number in footer: {len(footer_blocks)}, expected 4"
