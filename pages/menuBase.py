from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:
    title_products = (By.XPATH, "//span[text()='Products']")
    menu_hamburger = (By.ID, "react-burger-menu-btn")
    button_logout = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def is_title_found(self):
        try:
            title_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.title_products))
            return title_products.is_displayed()  #verificar se o elemento está visível e retorna True
        except:
            return False

    def click_menu_hamburger(self):
        self.driver.find_element(self.menu_hamburger).click()

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.button_logout)).click()

