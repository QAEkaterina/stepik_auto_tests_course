import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name').send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country").send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(30)
    browser.quit()