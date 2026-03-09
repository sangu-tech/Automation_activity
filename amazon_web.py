from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonSearchTest:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def open_amazon(self):
        self.driver.get("https://www.amazon.in")

    def search_product(self, product):
        search_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys(product)
        search_box.send_keys(Keys.RETURN)

        print("Search executed successfully")

    def close_browser(self):
        self.driver.quit()


# Run Test
test = AmazonSearchTest()
test.open_amazon()
test.search_product("laptop")
test.close_browser()