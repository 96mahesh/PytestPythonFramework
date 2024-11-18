import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setUp_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[text()='Login']").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"input-email").send_keys("amotooricap9@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "input-password").send_keys("1234")
        time.sleep(2)
        self. driver.find_element(By.XPATH,"//input[@value='Login']").click()
        actual_text = self.driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
        expected_text = "Edit your account information"
        print("actual text is : ",actual_text)
        assert actual_text.__eq__("Edit your account information")

    def test_login_with_Invalid_email_valid_password(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[text()='Login']").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"input-email").send_keys(self.genarate_email_with_time_stamp())
        time.sleep(2)
        self.driver.find_element(By.ID, "input-password").send_keys("1234")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        actual_Text = (self.driver.find_element
                       (By.XPATH,"//div[text()='Warning: No match for E-Mail Address and/or Password.']").text)
        print("actual text :",actual_Text)
        expected_Text = "Warning: No match for E-Mail Address and/or Password."
        assert expected_Text.__contains__(actual_Text)

    def test_login_with_valid_email_invalid_password(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-email").send_keys("amotooricap1@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "input-password").send_keys("123456789")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_Text = "Warning: No match for E-Mail Address and/or Password."
        actual_Text = self.driver.find_element(By.XPATH,
                                          "//div[text()='Warning: No match for E-Mail Address and/or Password.']").text
        print("actual text :", actual_Text)
        assert expected_Text.__contains__(actual_Text)

    def test_login_without_entering_credentials(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "input-email").send_keys(" ")
        time.sleep(2)
        self.driver.find_element(By.ID, "input-password").send_keys(" ")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_Text = "Warning: No match for E-Mail Address and/or Password."
        actual_Text = self.driver.find_element(By.XPATH,
                                          "//div[text()='Warning: No match for E-Mail Address and/or Password.']").text
        print("actual text :", actual_Text)
        assert expected_Text.__contains__(actual_Text)

    def genarate_email_with_time_stamp(self):
       cuttent_datetime =  datetime.now()
       time_stamp = cuttent_datetime.strftime("%y_%m_%d_%H_%M_%S")
       return "maheshram"+time_stamp+"@gmail.com"

   #time_stamp = datetime.now()..strftime("%y_%m_%d_%H_%M_%S")