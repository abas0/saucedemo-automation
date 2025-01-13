from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:
    text_complete_order = (By.CLASS_NAME, "complete-text")

    def __init__(self, driver):
        self.driver = driver

    def is_title_found(self):
        try:
            text_complete_order = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.text_complete_order))
            return text_complete_order.is_displayed()
        except:
            return False
