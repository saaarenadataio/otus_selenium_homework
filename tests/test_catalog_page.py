from page_objects.catalogue_page import Catalogue_Page


def test_catalog_page(driver):
    Catalogue_Page(driver).check_elements_on_page()
