from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
	return str ( math.log( abs( 12 * math.sin( int( x ) ) ) ) )

x_in_text = browser.find_element(By.ID, "input_value")
x_value = x_in_text.text

first_answer = calc(x_value)

try:
   first_input = browser.find_element(By.ID, "answer")
   browser.execute_script("return arguments[0].scrollIntoView(true);", first_input)

   first_input.send_keys(first_answer)

   robotCheckbox = browser.find_element(By.ID, "robotCheckbox").click()

   robotRadiobutton = browser.find_element(By.ID, "robotsRule").click()

   send_button = browser.find_element(By.CLASS_NAME, "btn-default").click()

finally:
    time.sleep(5)
    browser.quit()