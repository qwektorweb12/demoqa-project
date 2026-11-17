from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    TITLE_H1 = (By.XPATH, ".//h1")
    FULL_NAAME_FORM = (By.XPATH, ".//*[@id='username']")
    EMAIL_FORM = (By.XPATH, ".//*[@id='userEmail']")
    CURRENT_ADDRES = (By.XPATH, ".//*[@id='currentAddress']")
    PERMAMENT_ADDRES = (By.XPATH, ".//*[@id='permamentAddress']")
    BTN_SUBMIT = (By.XPATH, ".//*[@id='submit']")

