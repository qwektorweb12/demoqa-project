from abc import ABC


class BasePage(ABC):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    def input(self, locator, text):
        element = self.driver.find_element(*locator)
        element. send_keys(text)

    def click(self, locator):
        element = self.driverfind_element(*locator)
        element.click()
        