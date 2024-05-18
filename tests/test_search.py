import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@allure.feature('Search')
class TestSearch:

    @allure.title('Test Ebay Search Functionality')
    def test_ebay_search(self, driver):
        driver.get("https://www.ebay.com")
        search_box = driver.find_element(By.NAME, "_nkw")
        search_box.send_keys("Laptop")
        search_box.submit()
        assert "Laptop" in driver.title

    @allure.title('Basic Search')
    def test_basic_search(self, driver):
        driver.get("https://www.ebay.com")
        search_box = driver.find_element(By.ID, "gh-ac")
        search_box.send_keys("laptop")
        search_box.submit()
        assert "laptop" in driver.title.lower()
        assert driver.find_elements(By.CSS_SELECTOR, ".s-item")

    @allure.title('Search Button Functionality')
    def test_search_button_functionality(self, driver):
        driver.get("https://www.ebay.com")
        search_box = driver.find_element(By.ID, "gh-ac")
        search_box.send_keys("laptop")
        search_button = driver.find_element(By.ID, "gh-btn")
        search_button.click()
        assert "laptop" in driver.title.lower()
        assert driver.find_elements(By.CSS_SELECTOR, ".s-item")

    @allure.title('Test Search Result Pagination')
    def test_search_result_pagination(self, driver):
        driver.get("https://www.ebay.com/sch/i.html?_nkw=Laptop")
        pagination = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".pagination__items"))
        )
        assert pagination.is_displayed()
        next_button = driver.find_element(By.CSS_SELECTOR, ".pagination__next")
        next_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pagination__items")))

    @allure.title('Test Filter by Condition')
    def test_filter_by_condition(self, driver):
        driver.get("https://www.ebay.com/sch/i.html?_nkw=Laptop")
        new_condition_filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='New']"))
        )
        new_condition_filter.click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'New')]"))
        )
