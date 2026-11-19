from abc import ABC

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(ABC):

    def __init__(self, driver, time_out=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, time_out)

    def open(self, url):
        self.driver.get(url)

    @property
    def get_title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        element = self.find_element_with_visible(locator)
        return element.text
    
    def input(self, locator, text):
        element = self.find_element_with_visible(locator)
        element.send_keys(text)
    
    def click(self, locator):
        element = self.find_element_with_clickable(locator)
        element.click()
    
    def wait_presence_of_element_located(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_element_to_be_clickable(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_visibility_of_element_located(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def find_element_with_presence(self, locator):
        self.wait_presence_of_element_located(locator)
        element = self.driver.find_element(*locator)
        return element

    def find_element_with_clickable(self, locator):
        self.wait_element_to_be_clickable(locator)
        element = self.driver.find_element(*locator)
        return element

    def find_element_with_visible(self, locator):
        self.wait_visibility_of_element_locator(locator)
        element = self.driver.find_element(*locator)
        return element
    
    def remove_element_from_dom(self, locator):
        element = self.find_element_with_presence(locator)
        self.driver.execute_script("argument[0].remove().", element)

    def scroll_to(self, locator):
        element = self.find_element_with_presence(locator)
        self.driver.execute_script("argument[0].scrollIntoView(true);", element)
    
    def get_attribute(self, locator, attribute_name):
        element = self.wait_presence_of_element_located(locator)
        return element.get_attribute(attribute_name)
