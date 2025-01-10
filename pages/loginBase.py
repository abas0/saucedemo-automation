from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from base import Base


class LoginPage:
    url_login = 'https://www.saucedemo.com/'
    input_username = (By.ID, "user-name")
    input_password = (By.ID, "password")
    button_login = (By.ID, "login-button")
    title_products = (By.XPATH, "//span[text()='Products']")

    # invocando o __init da classe Base
    # driver=None porque não é necessário fornecer um driver diretamente ao instanciar a classe
    # o browser será fornecido
    def __init__(self, driver):
        self.driver = driver

    def open_login(self):
        self.driver.get(self.url_login)

    def click_login_button(self):
        # asterisco para desempacotar a tupla
        self.driver.find_element(*self.button_login).click()

    #def is_url_login(self):
    # return self.is_url(self.url_login)

    def insert_username(self, username):
        # tornar um timeout um default
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.input_username)
        ).send_keys(username)

    def insert_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.input_password)).send_keys(password)

    def is_title_found(self):
        try:
            title_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.title_products))
            return title_products.is_displayed()  #verificar se o elemento está visível e retorna True
        except:
            return False
