from selenium.webdriver.common.by import By


class CartPage:
    title_product_cart = (By.CSS_SELECTOR, ".cart_item_label "
                                           ".inventory_item_name ")

    def __init__(self, driver):
        self.driver = driver

    def is_length_greater_than_zero(self):
        title_product_cart = self.driver.find_elements(*self.title_product_cart)
        return len(title_product_cart)
