import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setUp_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.NAME,"search").send_keys("HP")
        self.driver.find_element(By.XPATH,"//button[contains(@class,'default')]").click()
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    def test_search_for_a_invalid_product(self):
        self.driver.find_element(By.NAME,"search").send_keys("Honda")
        self.driver.find_element(By.XPATH,"//button[contains(@class,'default')]").click()
        expectrs_text = "There is no product that matches the search criteria."
        actual_text = self.driver.find_element(By.XPATH,"//input[@id='button-search']//following-sibling::p").text
        assert expectrs_text.__eq__(actual_text)

    def test_with_out_entering_any_product(self):
        self.driver.find_element(By.NAME,"search").send_keys("Honda")
        self.driver.find_element(By.XPATH,"//button[contains(@class,'default')]").click()
        expectrs_text = "There is no product that matches the search criteria."
        actual_text = self.driver.find_element(By.XPATH,"//input[@id='button-search']//following-sibling::p").text
        assert expectrs_text.__eq__(actual_text)