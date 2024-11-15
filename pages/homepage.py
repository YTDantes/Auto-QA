from selenium.webdriver.common.by import By




class HomePage:


    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get("https://gorzdrav.org/")

    def click_gram(self):
        grammidin = self.driver.find_element(By.XPATH, "//a[text()='Граммидин с анестетиком Спрей для местного применения 112 доз']")
        grammidin.click()

    def click_button(self):
        popular_link = self.driver.find_element(By.CSS_SELECTOR, '[data-contentbody=".content_1"]')
        popular_link.click()

    def check_products_count(self, count):
        populars = self.driver.find_elements(By.XPATH, "//div[@class='js-products__tabs__content content_1']//div[@class='owl-item c-gallery__item']")
        assert len(populars) == count