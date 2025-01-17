from selenium import webdriver

from pages.cartBase import CartPage
from pages.loginBase import LoginPage
from pages.menuBase import MenuPage


class TestCT03:
    def test_adcionar_itens_carrinhos(self):
        self.driver = webdriver.Chrome()

        self.driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(self.driver)  # criando uma instância
        menu_page = MenuPage(self.driver)
        cart_page = CartPage(self.driver)

        login_page.insert_username("standard_user")
        login_page.insert_password("secret_sauce")
        login_page.click_login_button()

        assert menu_page.is_title_found(), "Elemento não está visível na página"

        menu_page.select_all_products()

        menu_page.scroll_to_element()
        menu_page.click_icon_cart()
        assert cart_page.get_length() > 0, "Elementos não encontrados"

        self.driver.quit()