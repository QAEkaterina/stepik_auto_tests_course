import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # time.sleep(3)
    browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000))).click()
    # time.sleep(3)

    input1 = browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name').send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country").send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(10)

finally:
    browser.quit()