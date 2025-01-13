from selenium.webdriver.common.by import By


class CartPage:
    title_product_cart = (By.CSS_SELECTOR, ".cart_item_label "
                                           ".inventory_item_name ")
    remove_button = (By.XPATH, "//button[text() = 'Remove']")
    button_checkout = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_length(self):
        title_product_cart = self.driver.find_elements(*self.title_product_cart)
        return len(title_product_cart)

    def remove_one_product(self):
        remove_button = self.driver.find_elements(*self.remove_button)
        remove_button[0].click()

    def click_checkout(self):
        self.driver.find_element(*self.button_checkout).click()
