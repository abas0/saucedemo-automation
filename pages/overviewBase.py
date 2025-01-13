from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OverviewPage:
    button_finish = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        button_finish = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.button_finish))
        button_finish.click()
