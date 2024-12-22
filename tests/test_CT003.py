import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCT03:
    def test_adcionar_itens_carrinhos(self):
        self.driver = webdriver.Chrome()

        self.driver.get("https://www.saucedemo.com/")
        wait_time = 10

        input_username = self.driver.find_element(by=By.ID, value="user-name")
        input_username.send_keys("standard_user")
        input_password = self.driver.find_element(by=By.ID, value="password")
        input_password.send_keys("secret_sauce")
        button_login = self.driver.find_element(by=By.ID, value="login-button")
        button_login.click()

        title_products = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Products']")))

        assert title_products.is_displayed(), "Elemento não está visível na página"

        button_add_cart = self.driver.find_elements(by=By.XPATH, value="//button[@class = 'btn btn_primary btn_small "
                                                                       "btn_inventory ']")
        title_product = self.driver.find_elements(by=By.CSS_SELECTOR, value=".inventory_item_label "
                                                                            ".inventory_item_name ")
        for i in range(0, len(button_add_cart)):
            button_add_cart[i].click()

        icon_cart = self.driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link")
        self.driver.execute_script("arguments[0].scrollIntoView();", icon_cart)
        icon_cart.click()
        title_product_cart = self.driver.find_elements(by=By.CSS_SELECTOR, value=".cart_item_label "
                                                                                 ".inventory_item_name ")
        assert len(title_product_cart) > 0, "Elementos não encontrado"

        self.driver.quit()