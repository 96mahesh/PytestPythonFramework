import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setUp_and_teardown")
class TestRegistration:
    def test_registor_with_mandotray_fields(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Mahesh")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Rampatruni")
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys(self.genarate_email_with_time_stamp())
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("9182853719")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("1234")
        self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        expected_test = "Your Account Has Been Created!'"
        assert self.driver.find_element(By.XPATH,"//h1[text()='Your Account Has Been Created!']").text.__contains__(expected_test)

    def test_registor_with_all_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Mahesh")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Rampatruni")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(self.genarate_email_with_time_stamp())
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("1234567893")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("1234")
        self.driver.find_element(By.XPATH,"//label[text()='Yes']").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_test = "Your Account Has Been Created!'"
        assert self.driver.find_element(By.XPATH, "//h1[text()='Your Account Has Been Created!']").text.__contains__(
            expected_test)

    def test_registor_with_duplicate_email(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Mahesh")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Rampatruni")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("amotooricap1@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("1234567893")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("1234")
        self.driver.find_element(By.XPATH, "//label[text()='Yes']").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_test = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[text()='Warning: E-Mail Address is already registered!']").text.__contains__(
            expected_test)

    def test_registor_with_out_entring_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_test = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH,
                                   "//div[@id='account-register']//div[text()='Warning: You must agree to the Privacy Policy!']").text.__contains__(
            expected_test)
        expected_fristName_text = 'First Name must be between 1 and 32 characters!'
        assert self.driver.find_element(By.XPATH,"//input[@id='input-firstname']//following-sibling::div").text.__contains__(expected_fristName_text)
        expected_lastName_text = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']//following-sibling::div").text.__contains__(expected_lastName_text)
        expected_email_text = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-email']//following-sibling::div").text.__contains__(expected_email_text)
        expected_telephone_text = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']//following-sibling::div").text.__contains__(
            expected_telephone_text)
        expected_password_text = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-password']//following-sibling::div").text.__contains__(
            expected_password_text)
    def genarate_email_with_time_stamp(self):
        cuttent_datetime = datetime.now()
        time_stamp = cuttent_datetime.strftime("%y_%m_%d_%H_%M_%S")
        return "maheshram" + time_stamp + "@gmail.com"
