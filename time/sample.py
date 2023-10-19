from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# Find an input element by its ID and enter text
input_element = driver.find_element(By.ID, "user-message")
input_element.send_keys("My message!")

# Pause using time.sleep()
time.sleep(5)

# Find an element by its ID and click on it
element = driver.find_element(By.ID, "showInput")
element.click()

# Pause using time.sleep()
time.sleep(5)

# Close the browser
driver.quit()
