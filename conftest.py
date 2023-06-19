import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", action="store", default="http://localhost")
    parser.addoption("--driver_storage", default="/home/asm/Downloads/drivers")
    parser.addoption("--headless", action="store_true")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver_storage = request.config.getoption("--driver_storage")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    _driver = None

    if browser_name in ["firefox", "ff"]:
        _driver = webdriver.Firefox(executable_path=f"{driver_storage}/geckodriver")
    elif browser_name == "chrome":
        _driver = webdriver.Chrome(executable_path=f"{driver_storage}/chromedriver")

    _driver.maximize_window()

    _driver.get(url)
    driver.url = url

    yield _driver

    _driver.close()
