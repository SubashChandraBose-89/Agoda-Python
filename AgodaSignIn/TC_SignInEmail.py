import unittest
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SigninEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.agoda.com/")
        self.driver.maximize_window()

    def test_blankEmailLogin(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.popup_1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close Message']")))
        self.popup_1.click()
        self.driver.find_element(By.XPATH, '//span[@class="Box-sc-kv6pi1-0 bTkTcE"]').click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "email").send_keys(" ")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='sc-fzoiQi hsJTpM']").click()
        print("Login Button Clicked [1]")
        time.sleep(5)
        self.label_text = self.driver.find_element(By.XPATH, "//span[@class='sc-fznZeY PbGWn']")
        self.actual_result = self.label_text.text
        print(self.actual_result)
        self.expect_result = "Email address format is not valid."
        self.assertTrue(self.actual_result == self.expect_result), 'Test Failed'
        print("Blank Login Alert is Successful")

    def test_validEmailLogin(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.popup_1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close Message']")))
        self.popup_1.click()
        self.driver.find_element(By.XPATH, '//span[@class="Box-sc-kv6pi1-0 bTkTcE"]').click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "email").send_keys("subashchandrabose0289@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Subash@777")
        self.driver.find_element(By.XPATH, "//button[@class='sc-fzoiQi hsJTpM']").click()
        print("Login Button Clicked [2]")
        time.sleep(3)
        try:
            self.popup_2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button[@class='ab-close-button']")))
            self.popup_2.click()
        except TimeoutException:
            print("PopUp Alert is Not Appear")
            time.sleep(2)
        self.user_name = self.driver.find_element(By.XPATH,
                                                  "//p[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 Hkrzy kite-js-Typography ']")
        self.actual_text = self.user_name.text
        self.expectd_text = "Subash C."
        self.assertTrue(self.actual_text == self.expectd_text), "Test Failed"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
