import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@allure.feature('Navigation')
class TestNavigation:

    @allure.title('Test Ebay Navigation Bar Links')
    def test_ebay_navigation_bar_links(self, driver):
        driver.get("https://www.ebay.com")
        assert driver.find_element(By.LINK_TEXT, "Electronics")
        assert driver.find_element(By.LINK_TEXT, "Saved")
        assert driver.find_element(By.LINK_TEXT, "Motors")

    @allure.title('Test Ebay Community')
    def test_ebay_community(self, driver):
        driver.get("https://www.ebay.com")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        wait = WebDriverWait(driver, 30)
        footer_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gf-BIG"]/table/tbody/tr/td[5]/ul[2]/li[2]/a')))
        footer_link.click()
        assert "eBay Community" in driver.title

    @allure.title('Logo Link Test')
    def test_logo_link(self, driver):
        driver.get("https://www.ebay.com")
        logo = driver.find_element(By.ID, "gh-la")
        logo.click()
        assert driver.current_url == "https://www.ebay.com/"

    @allure.title('Category Navigation')
    def test_category_navigation(self, driver):
        driver.get("https://www.ebay.com")
        category_link = driver.find_element(By.LINK_TEXT, "Electronics")
        category_link.click()
        assert "Electronics" in driver.title

    @allure.title('Sub-category Navigation')
    def test_sub_category_navigation(self, driver):
        driver.get("https://www.ebay.com/b/Electronics/bn_7000259124")
        sub_category_link = driver.find_element(By.LINK_TEXT, "Cell Phones & Accessories")
        sub_category_link.click()
        assert "Cell Phones & Accessories" in driver.title
