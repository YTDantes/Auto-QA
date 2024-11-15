from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_gram(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_gram()
    product_page = ProductPage(driver)
    product_page.check_title_is("Граммидин с анестетиком Спрей для местного применения 112 доз")



def test_popular(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_button()
    homepage.check_products_count(6)