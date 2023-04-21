import time
import unittest
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NightHotelSelect(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.agoda.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 40)

    def test_nightBook(self):
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
        self.city_name = self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, "//input[@class='SearchBoxTextEditor SearchBoxTextEditor--autocomplete']")))
        self.city_name.send_keys("Chennai")
        print("City Name Printed")
        self.city_select = self.driver.find_element(By.XPATH,
                                                    "//li[@class='Suggestion Suggestion__categoryName'][@data-text='Chennai'][@data-element-search-type='1']")
        self.city_select.click()
        self.date_from = self.driver.find_element(By.XPATH, "//span[@class='PriceSurgePicker-Day__label PriceSurgePicker-Day__label--wide' and text()='20']")
        self.click_datefm = self.wait.until(EC.element_to_be_clickable(self.date_from))
        self.click_datefm.click()
        self.date_to = self.driver.find_element(By.XPATH, "//span[@class='PriceSurgePicker-Day__label PriceSurgePicker-Day__label--wide' and text()='26']")
        self.click_dateto = self.wait.until(EC.element_to_be_clickable(self.date_to))
        self.click_dateto.click()
        print("Date Selected")
        if (self.driver.find_element(By.XPATH, "//div[@id='occupancy-box']")).is_displayed():
            self.driver.find_element(By.XPATH, "//div[@id='occupancy-box']").click()
            print("Number of Rooms Booked")
            self.driver.find_element(By.XPATH,
                                     "//button[@class='Buttonstyled__ButtonStyled-sc-5gjk6l-0 hKHQVh Box-sc-kv6pi1-0 "
                                     "fDMIuA']").click()
            print("Search Button Clicked")
        else:
            print("DropDown Error")
        self.actual_text = self.driver.page_source
        self.expted_text = "SearchPage"
        if self.expted_text in self.actual_text:
            print("Night Stay Booking function is Successful")
        self.click_hotel = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//h3[@data-selenium='hotel-name'][@class='sc-jrAGrp sc-kEjbxe eDlaBj dscgss']")))
        self.click_hotel_text = self.click_hotel.text
        print("Name of the Hotel :" + self.click_hotel_text)
        self.click_hotel.click()
        print("Hotel selected")
        self.window_handle = self.driver.window_handles
        print(self.window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Switched to new window")
        time.sleep(3)
        self.booknow_button = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                                "//button[@class='ChildRoomsList-bookButtonInput'][@data-element-master-room-id='3343939']")))
        if self.booknow_button.is_displayed():
            try:
                self.booknow_button.click()
            except NoSuchElementException:
                print("Book now button not found")
        else:
            self.regnow_button = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                                   "//button[@data-element-crossedout-rate='19999'][@data-element-master-room-id='15157221'][1]")))
            self.regnow_button.click()
            print("Register Button Found")
        print("hotel selected")
        time.sleep(2)
        self.next_stepbook = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='Buttonstyled__ButtonStyled-sc-5gjk6l-0 kQOJVT sc-pZOBi gagPGR']")))
        self.next_stepbook.click()
        print("Hotel Booked for Overnight")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
