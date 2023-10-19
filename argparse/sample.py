import argparse
from selenium import webdriver

# Define Arguments
parser = argparse.ArgumentParser(description='Selenium Test Script')
parser.add_argument('--url', required=True, help='URL for testing')
parser.add_argument('--browser', required=True, help='Browser for testing')

# Parse Arguments
args = parser.parse_args()

# Access Argument Values
url = args.url
browser = args.browser

# Initialize WebDriver based on provided browser
if browser == 'Chrome':
    driver = webdriver.Chrome()
elif browser == 'Firefox':
    driver = webdriver.Firefox()
else:
    raise ValueError(f'Unsupported browser: {browser}')

# Navigate to the provided URL
driver.get(url)

# Don't forget to close the WebDriver after testing is complete
driver.quit()