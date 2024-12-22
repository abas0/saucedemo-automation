from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCT02:
    def test_logout(self):
        self.driver = webdriver.Chrome()

        self.driver.get("https://www.saucedemo.com/")
        wait_time = 10

        input_username = self.driver.find_element(by=By.ID, value="user-name")
        input_username.send_keys("standard_user")
        input_password = self.driver.find_element(by=By.ID, value="password")
        input_password.send_keys("secret_sauce")
        button_login = self.driver.find_element(by=By.ID, value="login-button")
        button_login.click()

        # time.sleep(5)
        title_products = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Products']")))

        assert title_products.is_displayed(), "Elemento não está visível na página"

        button_menu_hamburger = self.driver.find_element(by=By.ID, value="react-burger-menu-btn")
        button_menu_hamburger.click()

        button_logout = WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        button_logout.click()

        title_swag_labs = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login_logo")))

        assert title_swag_labs.is_displayed(), "Elemento não está visível na página"