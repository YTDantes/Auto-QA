from selenium.webdriver.common.by import By



class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        page_title = self.driver.find_element(By.XPATH, "//h1[text()='Граммидин с анестетиком Спрей для местного применения 112 доз']")
        assert page_title.text == title

