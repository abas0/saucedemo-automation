from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.loginBase import LoginPage
from pages.menuBase import MenuPage


class TestCT02:
    def test_logout(self):
        self.driver = webdriver.Chrome()

        self.driver.get("https://www.saucedemo.com/")
        # wait_time = 10
        login_page = LoginPage(self.driver)  # criando uma instância
        menu_page = MenuPage(self.driver)
        login_page.insert_username("standard_user")
        login_page.insert_password("secret_sauce")
        login_page.click_login_button()

        assert menu_page.is_title_found(), "Elemento não está visível na página"
        menu_page.click_menu_hamburger()

        menu_page.click_logout()

        assert login_page.is_title_found(), "Elemento não está visível na página"

        self.driver.quit()
