from selenium.webdriver.remote.webdriver import WebDriver


class TestClass(object):

    def test_chrome(self, selenium: WebDriver):
        selenium.implicitly_wait(10)
        selenium.get("https://google.com")
        queryInput = selenium.find_element_by_name("q")
        queryInput.send_keys("hello world wiki")
        queryInput.submit()
        resultStats = selenium.find_element_by_id("resultStats")
        if "About" not in resultStats.text:
            assert False

    def test_chrome2(self, selenium: WebDriver):
        selenium.implicitly_wait(10)
        selenium.get("https://google.com")
        queryInput = selenium.find_element_by_name("q")
        queryInput.send_keys("hello world wiki")
        queryInput.submit()
        firstResult = selenium.find_element_by_xpath("//*[@id=\"rso\"]/div/div/div[1]/div/div/h3/a")
        firstResult.click()
        if "Wikipedia" not in selenium.title:
            assert False

