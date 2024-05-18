import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature('Testing Ebay')
@allure.story('Basic functionality tests')
class TestEbay:
    
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

    @pytest.mark.skip(reason="Skipping the sign-in test") #skipped
    @allure.title('Test Ebay Login')
    def test_ebay_login(self, driver):
        driver.get("https://www.ebay.com")
        login_button = driver.find_element(By.XPATH, '//*[@id="gh-ug"]/a')
        login_button.click()
        driver.find_element(By.ID, "userid").send_keys("mukh_1534")
        driver.find_element(By.ID, "signin-continue-btn").click()
        driver.find_element(By.ID, "pass").send_keys("<password>")
        driver.find_element(By.ID, "sgnBt").click()
        assert "Muhit Khan" in driver.find_element(By.XPATH, '//*[@id="gh-ug"]/b[1]').text

    @allure.title('Test Ebay Search Functionality') 
    def test_ebay_search(self, driver):
        driver.get("https://www.ebay.com")
        search_box = driver.find_element(By.NAME, "_nkw")
        search_box.send_keys("Laptop")
        search_box.submit()
        assert "Laptop" in driver.title

    @allure.title('Test Ebay Navigation Bar Links') 
    def test_ebay_navigation_bar_links(self, driver):
        driver.get("https://www.ebay.com")
        # Assert the presence of navigation bar links
        assert driver.find_element(By.LINK_TEXT, "Electronics")
        assert driver.find_element(By.LINK_TEXT, "Saved")
        assert driver.find_element(By.LINK_TEXT, "Motors")

    @allure.title('Test Ebay Footer Links') 
    def test_ebay_footer_links(self, driver):
        driver.get("https://www.ebay.com")
        # Assert the presence of navigation footer links
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        wait = WebDriverWait(driver, 30)
        footer_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gf-BIG"]/table/tbody/tr/td[5]/ul[2]/li[2]/a')))
        expected_text = "eBay Community"
        assert expected_text in footer_link.text

    @allure.title('Test Ebay Community') 
    def test_ebay_community(self, driver):
        driver.get("https://www.ebay.com")
        # Assert the presence of navigation footer links
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

    @allure.title('Search Field Presence') 
    def test_search_field_presence(self, driver):
        driver.get("https://www.ebay.com")
        assert driver.find_element(By.ID, "gh-ac").is_displayed()

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

    @allure.title('Category Navigation') 
    def test_category_navigation(self, driver):
        driver.get("https://www.ebay.com")
        category_link = driver.find_element(By.LINK_TEXT, "Electronics")
        category_link.click()
        assert "Electronics" in driver.title

    @allure.title('Footer Links Presence')     
    def test_footer_links_presence(self, driver):
        driver.get("https://www.ebay.com")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        footer_links = driver.find_elements(By.CSS_SELECTOR, "#gf-BIG a")
        assert len(footer_links) > 0

    @allure.title('Product Listing Presence') 
    def test_product_listing_presence(self, driver):
        driver.get("https://www.ebay.com/sch/i.html?_nkw=laptop")
        assert driver.find_elements(By.CSS_SELECTOR, ".s-item")

    @allure.title('Sub-category Navigation') 
    def test_sub_category_navigation(self, driver):
        driver.get("https://www.ebay.com/b/Electronics/bn_7000259124")
        sub_category_link = driver.find_element(By.LINK_TEXT, "Cell Phones & Accessories")
        sub_category_link.click()
        assert "Cell Phones & Accessories" in driver.title
        
    @allure.title('Product Image Display')
    def test_product_image_display(self, driver):
        driver.get("https://www.ebay.com/sch/i.html?_nkw=laptop")
        product_image = driver.find_element(By.CSS_SELECTOR, ".s-item__image-img")
        assert product_image.is_displayed()

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