import time
from abc import ABC

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC



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

    def wait_presence_of_element_located(self, locator):
        self.wait.until(EC.presence_of_element_located)

    def wait_element_to_be_clickable(self, located):
        self.wait.until(EC.element_to_be_clickable)

    def wait_visibility_of_element_locator(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def find_element_with_presence(self, locator):
        self.wait_presence_of_element_located(locator)
        element = self.driver.find_element(locator)    
        return element

    def find_element_with_clickable(self, locator):
        self.wait_presence_to_be_clickable(locator)
        element = self.driver.find_element(*locator)
        return self.driver.find_element(locator)

    def find_element_with_visible(self, locator):
        self.wait_visibility_of_element_locator(locator)
        element = self.driver.find_element(*locator)
        return element
    