from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    TITLE_H1 = (By.XPATH, ".//h1")
    FULL_NAME_FORM = (By.XPATH, ".//input[@id='userName']")
    EMAIL_FORM = (By.XPATH, ".//input[@id='userEmail']")
    CURRENT_ADDRESS_FORM = (By.XPATH, ".//input[@id='currentAddress']")
    PERMANENT_ADDRESS_FORM = (By.XPATH, ".//input[@id='permanentAddress']")
    BTN_SUBMIT = (By.XPATH, ".//button[@id='submit']")
    FULL_NAME_TEXT = (By.XPATH, ".//p[@id='name']")
    EMAIL_TEXT = (By.XPATH, ".//p[@id='email']")
    CURRENT_ADDRESS_TEXT = (By.XPATH, ".//p[@id='currentAddress']")
    PERMANENT_ADDRESS_TEXT = (By.XPATH, ".//p[@id='permanentAddress']")
    DATA = (By.XPATH, ".//div[@id='output']")

    def fill_up_full_name(self, full_name):
        self.input(TextBoxPage.FULL_NAME_FORM, full_name)
    
    def fill_up_email(self, email):
        self.input(TextBoxPage.EMAIL_FORM, email)

    def fill_up_current_address(self, current_address):
        self.input(TextBoxPage.CURRENT_ADDRESS_FORM, current_address)
    
    def fill_up_permanent_address(self, permanent_address):
        self.input(TextBoxPage.PERMANENT_ADDRESS_FORM, permanent_address)
    
    def scroll_to_submit_button(self):
        self.scroll_to(TextBoxPage.BTN_SUBMIT)

    def click_submit(self):
        self.click(TextBoxPage.BTN_SUBMIT)

    def get_full_name(self):
        return self.get_text(TextBoxPage.FULL_NAME_TEXT)
    
    def get_email(self):
        return self.get_text(TextBoxPage.EMAIL_TEXT)
    
    def get_current_address(self):
        return self.get_text(TextBoxPage.CURRENT_ADDRESS_FORM)
    
    def get_permanent_address(self):
        return self.get_text(TextBoxPage.PERMANENT_ADDRESS_FORM)
    
    def get_full_data(self):
        return self.get_text(TextBoxPage.DATA)
    
    def is_border_email_red(self):
        return 'field-error' in self.get_attribute(TextBoxPage.EMAIL_FORM, 'class')
        