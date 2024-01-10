from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/simple_form_find_task.html'
driver = webdriver.Chrome()
driver.get(link)

try:
    driver.get(link)
    input1 = driver.find_element(By.NAME, 'first_name').send_keys("Ivan")

    input2 = driver.find_element(By.NAME,'last_name').send_keys("Petrov")

    input3 = driver.find_element(By.XPATH,'/html/body/div/form/div[3]/input').send_keys("Smolensk")

    input4 = driver.find_element(By.ID, 'country').send_keys("Russia")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(30)

    driver.quit()