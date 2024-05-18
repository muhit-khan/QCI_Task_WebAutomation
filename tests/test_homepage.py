import pytest
import allure
from selenium.webdriver.common.by import By

@allure.feature('Homepage')
class TestHomepage:

    @allure.title('Homepage Load Test')
    def test_homepage_load(self, driver):
        driver.get("https://www.ebay.com")
        assert driver.find_element(By.ID, "gh-la").is_displayed()  # eBay logo
        assert driver.find_element(By.ID, "gh-ac").is_displayed()  # Search bar
        assert driver.find_element(By.ID, "mainContent").is_displayed()  # Main content area

    @allure.title('Test Ebay Home Page Title')
    def test_ebay_home_page_title(self, driver):
        driver.get("https://www.ebay.com")
        assert "eBay" in driver.title
