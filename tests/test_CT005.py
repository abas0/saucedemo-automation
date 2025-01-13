from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.cartBase import CartPage
from pages.checkoutCompleteBase import CheckoutCompletePage
from pages.informationBase import InformationPage
from pages.loginBase import LoginPage
from pages.menuBase import MenuPage
from pages.overviewBase import OverviewPage


class TestCT05:
    def test_buy_product(self):
        self.driver = webdriver.Chrome()

        self.driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(self.driver)  # criando uma instância
        menu_page = MenuPage(self.driver)
        cart_page = CartPage(self.driver)
        information_page = InformationPage(self.driver)
        overview_page = OverviewPage(self.driver)
        checkout_complete_page = CheckoutCompletePage(self.driver)

        login_page.insert_username("standard_user")
        login_page.insert_password("secret_sauce")
        login_page.click_login_button()

        assert menu_page.is_title_found(), "Elemento não está visível na página"

        menu_page.select_one_product()

        menu_page.scroll_to_element()
        menu_page.click_icon_cart()
        assert cart_page.get_length() > 0, "Elementos não encontrados"

        cart_page.click_checkout()
        information_page.insert_first_name("Fulano")
        information_page.insert_last_name("da Silva")
        information_page.insert_postal_code("12345")
        information_page.click_continue()
        overview_page.click_finish()

        assert checkout_complete_page.is_title_found(), "Elemento não está visível na página"

        self.driver.quit()