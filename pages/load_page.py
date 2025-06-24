from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoadPage:
    URL = "https://shubhamsfit.github.io/Project-Website-One/"
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 9)

    def load(self):
        self.driver.get(self.URL)
    
    # def find(self, locator):
    #     return self.wait.until(EC.visibility_of_element_located(locator))

    # def type(self, locator, text):
    #     self.find(locator).send_keys(text)

    # def click(self, locator):
    #     self.find(locator).click()

    # def get_title(self):
    #     return self.driver.title