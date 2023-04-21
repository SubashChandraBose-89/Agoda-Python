# Test Case 001
# Verify the login logout function in Agoda
# 1, Open Web Browser(Chrome)
# 2, Open URL https://www.agoda.com/
# 3, Click SignIn Button
# 4, Enter Username
# 5, Enter Password
# 6, Click Login
# 7, Click SignOut
# 8, Capture the text in the SignIn button
# 9, Verify with the expected text: "Sign in"
# 10, Close
import time
import unittest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginEmail(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.agoda.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_LoginLogout(self):
        self.popup_1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close Message']")))
        self.popup_1.click()
        self.driver.find_element(By.XPATH, '//span[@class="Box-sc-kv6pi1-0 bTkTcE"]').click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "email").send_keys("subashchandrabose0289@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Subash@777")
        self.driver.find_element(By.XPATH, "//button[@class='sc-fzoiQi hsJTpM']").click()
        print("Login Button Clicked")
        time.sleep(3)
        try:
            self.popup_2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='ab-close-button']")))
            self.popup_2.click()
        except TimeoutException:
            print("PopUp Alert is Not Appear")
            time.sleep(2)
        self.signout_header = self.driver.find_element(By.XPATH, "//div[@class='UserMenustyled__UserMenuDisplay-sc-14cll85-1 hJSdLP'][@data-element-name='user-menu']")
        self.signout_header.click()
        self.driver.find_element(By.XPATH, "//button[@class='Buttonstyled__ButtonStyled-sc-5gjk6l-0 jxFsnW'][@data-element-name='sign-out-btn']").click()
        print("Logout Done Successfully")
        self.signin_element = self.driver.find_element(By.XPATH, "//span[@class='Box-sc-kv6pi1-0 bTkTcE']")
        self.actual_text = self.signin_element.text
        self.expectd_text = "Sign in"
        self.assertTrue(self.actual_text==self.expectd_text), "Test Failed"
        print("Login Logout Successful")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

