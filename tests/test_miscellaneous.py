import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Miscellaneous')
class TestMiscellaneous:

    @allure.title('Test Ebay Login')
    @pytest.mark.skip(reason="Skipping the sign-in test for Credential Security")
    def test_ebay_login(self, driver):
        driver.get("https://www.ebay.com")
        login_button = driver.find_element(By.XPATH, '//*[@id="gh-ug"]/a')
        login_button.click()
        driver.find_element(By.ID, "userid").send_keys("mukh_1534")
        driver.find_element(By.ID, "signin-continue-btn").click()
        driver.find_element(By.ID, "pass").send_keys("<password>")
        driver.find_element(By.ID, "sgnBt").click()
        assert "Muhit Khan" in driver.find_element(By.XPATH, '//*[@id="gh-ug"]/b[1]').text

    @allure.title('Product Listing Presence')
    def test_product_listing_presence(self, driver):
        driver.get("https://www.ebay.com/sch/i.html?_nkw=laptop")
        assert driver.find_elements(By.CSS_SELECTOR, ".s-item")

    @allure.title('Product Image Display')
    def test_product_image_display(self, driver):
        driver.get("https://www.ebay.com/sch/i.html?_nkw=laptop")
        product_image = driver.find_element(By.CSS_SELECTOR, ".s-item__image-img")
        assert product_image.is_displayed()

    @allure.title('Test Advanced Search Link')
    def test_advanced_search_link(self, driver):
        driver.get("https://www.ebay.com")
        advanced_search_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Advanced"))
        )
        assert advanced_search_link.is_displayed()
        advanced_search_link.click()
        WebDriverWait(driver, 10).until(EC.title_contains("Advanced Search"))

    @allure.title('Test Daily Deals Link')
    def test_daily_deals_link(self, driver):
        driver.get("https://www.ebay.com")
        daily_deals_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Daily Deals"))
        )
        assert daily_deals_link.is_displayed()
        daily_deals_link.click()
        WebDriverWait(driver, 10).until(EC.title_contains("Daily Deals"))

    @allure.title('Test Selling on eBay Link')
    def test_selling_on_ebay_link(self, driver):
        driver.get("https://www.ebay.com")
        sell_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sell"))
        )
        assert sell_link.is_displayed()
        sell_link.click()
        WebDriverWait(driver, 10).until(EC.title_contains("Sell"))

    @allure.title('Test Sign Out Button Presence')
    def test_sign_out_button_presence(self, driver):
        driver.get("https://www.ebay.com")
        sign_out_button = driver.find_elements(By.LINK_TEXT, "Sign out")
        assert len(sign_out_button) == 0

    @allure.title('Test Accessibility Statement Link')
    def test_accessibility_statement_link(self, driver):
        driver.get("https://www.ebay.com")
        accessibility_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Accessibility"))
        )
        assert accessibility_link.is_displayed()
        accessibility_link.click()
        WebDriverWait(driver, 10).until(EC.title_contains("Accessibility"))
