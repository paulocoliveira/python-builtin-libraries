import unittest
import configparser
import os
import shutil
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load the configuration file
config = configparser.ConfigParser()
config.read('config/config.ini')

class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        username = os.getenv("LT_USERNAME")
        accessKey = os.getenv("LT_ACCESS_KEY")

        gridUrl = config.get('CLOUDGRID', 'grid_url')

        web_driver = webdriver.ChromeOptions()
        platform = config.get('ENV', 'platform')
        browser_name = config.get('ENV', 'browser_name')

        lt_options = {
            "user": username,
            "accessKey": accessKey,
            "build": config.get('CLOUDGRID', 'build_name'),
            "name": config.get('CLOUDGRID', 'test_name'),
            "platformName": platform,
            "w3c": config.get('CLOUDGRID', 'w3c'),
            "browserName": browser_name,
            "browserVersion": config.get('CLOUDGRID', 'browser_version'),
            "selenium_version": config.get('CLOUDGRID', 'selenium_version'),
            "visual": True
        }

        options = web_driver
        options.set_capability('LT:Options', lt_options)
        
        url = f"https://{username}:{accessKey}@{gridUrl}"
        
        self.driver = webdriver.Remote(
            command_executor=url,
            options=options
        )

        self.driver.get(config.get('WEBSITE', 'url'))
        self.driver.maximize_window()
        
        self.input_element = self.driver.find_element(By.ID, "user-message")
        self.button = self.driver.find_element(By.ID, "showInput")
        self.message_element = self.driver.find_element(By.ID, "message")
    
    def tearDown(self):
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime('%Y-%m-%d-%H-%M-%S')
        shutil.copytree('./config', f"{formatted_date}-backup")
        self.driver.quit()