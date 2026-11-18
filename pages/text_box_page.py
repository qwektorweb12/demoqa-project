from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    TITLE_H1 = (By.XPATH, ".//h1")
    FULL_NAME_FORM = (By.XPATH, ".//*[@id='username']")
    EMAIL_FORM = (By.XPATH, ".//*[@id='userEmail']")
    CURRENT_ADDRES = (By.XPATH, ".//*[@id='currentAddress']")
    PERMAMENT_ADDRES = (By.XPATH, ".//*[@id='permamentAddress']")
    BTN_SUBMIT = (By.XPATH, ".//*[@id='submit']")

    def fill_up_full_name(self, full_name):
        self.input(TextBoxPage.FULL_NAME_FORM, full_name)

    def fill_up_email(self, email):
        self.input(TextBoxPage.EMAIL_FORM, email)

    def fill_up_current_address(self, current_address):
        self.input(TextBoxPage.CURRENT_ADDRESS_FORM, current_address)

    def fill_up_permament_address(self, permament_address):
        self.input(TextBoxPage.PERMAMENT_ADDRESS_FORM, permament_address)

    def click_submit(self):
        self.click(TextBoxPage.BTN_SUBMIT)        