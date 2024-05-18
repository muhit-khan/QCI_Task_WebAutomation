import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@allure.feature('Footer')
class TestFooter:

    @allure.title('Test Ebay Footer Links')
    def test_ebay_footer_links(self, driver):
        driver.get("https://www.ebay.com")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        wait = WebDriverWait(driver, 30)
        footer_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gf-BIG"]/table/tbody/tr/td[5]/ul[2]/li[2]/a')))
        expected_text = "eBay Community"
        assert expected_text in footer_link.text

    @allure.title('Footer Links Presence')
    def test_footer_links_presence(self, driver):
        driver.get("https://www.ebay.com")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        footer_links = driver.find_elements(By.CSS_SELECTOR, "#gf-BIG a")
        assert len(footer_links) > 0

