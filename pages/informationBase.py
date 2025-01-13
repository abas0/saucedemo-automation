from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InformationPage:
    input_first_name = (By.ID, "first-name")
    input_last_name = (By.ID, "last-name")
    input_postal_code = (By.ID, "postal-code")
    button_continue = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def insert_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.input_first_name)
        ).send_keys(first_name)

    def insert_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.input_last_name)
        ).send_keys(last_name)

    def insert_postal_code(self, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.input_postal_code)
        ).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.button_continue).click()
