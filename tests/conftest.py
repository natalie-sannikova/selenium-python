import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Firefox


@pytest.fixture
def selenium(selenium: WebDriver):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


@pytest.fixture
def capabilities():
    capabilities = None
    return capabilities


@pytest.fixture
def driver(capabilities):
    driver = Firefox(capabilities=capabilities)
    yield driver
    driver.quit()