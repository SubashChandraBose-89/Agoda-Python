#Test Case 002
# Verify Day Use Stays Booking
# 1, Open Web Browser(Chrome)
# 2, Open URL https://www.agoda.com/
# 3, Click SignIn Button
# 4, Enter Username
# 5, Enter Password
# 6, Click Login
# 7, Click "Day Use Stays" button
# 8, Clear the City Search Tab and Enter City Name "Chennai"
# 9, Select "Chennai"
# 10, Select a CheckIn date for one adult
# 11, Click Search button
# 12, Verify the expected "SearchPage" text in page_source
# 13, Day Use Booking function is Successful

import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DayUseStay(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.agoda.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_dayBook(self):
        self.popup_1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close Message']")))
        self.popup_1.click()
        self.driver.find_element(By.XPATH, '//span[@class="Box-sc-kv6pi1-0 bTkTcE"]').click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "email").send_keys("subashchandrabose0289@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Subash@777")
        self.driver.find_element(By.XPATH, "//button[@class='sc-fzoiQi hsJTpM']").click()
        print("Login Button Clicked")
        time.sleep(2)
        try:
            self.popup_2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button[@class='ab-close-button']")))
            self.popup_2.click()
        except TimeoutException:
            print("PopUp Alert is Not Appear")
            time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//button[@data-element-name='funnel-switcher' and @data-hh-booking-duration-type='1' and @color='primary']//span[@class='Spanstyled__SpanStyled-sc-16tp9kb-0 kkSkZk kite-js-Span ']").click()
            print("Day Stay Selected")
        except NoSuchElementException:
            self.driver.find_element(By.XPATH, "//button[@aria-pressed='false' and @data-element-name='funnel-switcher' and @data-hh-booking-duration-type='1']").click()
            print("DayStay Second element found")
        self.city_name = self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, "//input[@class='SearchBoxTextEditor SearchBoxTextEditor--autocomplete']")))
        self.city_name.send_keys("Chennai")
        print("City Name Printed")
        self.city_select = self.driver.find_element(By.XPATH, "//li[@class='Suggestion Suggestion__categoryName'][@data-text='Chennai'][@data-element-search-type='1']")
        self.city_select.click()
        self.date_from = self.driver.find_element(By.XPATH, "//span[@class='DayPicker-Day__label'][@data-selenium-date='2023-04-20']")
        self.click_date = self.wait.until(EC.element_to_be_clickable(self.date_from))
        self.click_date.click()
        print("Date Selected")
        if (self.driver.find_element(By.XPATH, "//div[@id='occupancy-box']")).is_displayed():
            self.driver.find_element(By.XPATH, "//div[@id='occupancy-box']").click()
            print("Number of Rooms Booked")
            #time.sleep(5)
            self.driver.find_element(By.XPATH, "//button[@class='Buttonstyled__ButtonStyled-sc-5gjk6l-0 hKHQVh Box-sc-kv6pi1-0 "
                                          "fDMIuA']").click()
            print("Search Button Clicked")
        else:
            print("DropDown Error")
        self.actual_text = self.driver.page_source
        self.expted_text = "SearchPage"
        if self.expted_text in self.actual_text:
            print("Day Use Booking function is Successful")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
