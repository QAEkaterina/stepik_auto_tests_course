import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


firstname = browser.find_element(By.XPATH, '//input[contains(@name, "firstname")]')
lastname = browser.find_element(By.XPATH, '//input[contains(@name, "lastname")]')
email = browser.find_element(By.XPATH, '//input[contains(@name, "email")]')
file = browser.find_element(By.XPATH, '//input[contains(@name, "file")]')

button = browser.find_element(By.XPATH, '//button[contains(@class, "btn btn-primary")]')

firstname.send_keys("firstname")
lastname.send_keys("lastname")
email.send_keys("email")
file.send_keys(r"C:\Users\Катя\123.txt")

button.click()

time.sleep(10)