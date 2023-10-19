import unittest
import time
import csv
import json
import logging
from datetime import datetime
import string
import sys
import random
import locale
import math
import pickle
import re
from TestBase.WebDriverSetup import WebDriverSetup

# Initialize the logger
logger = logging.getLogger('TestLogger')
logger.setLevel(logging.DEBUG)

class TestFormLabels(WebDriverSetup):
  
    def test_random_strings(self):       
        characters = string.ascii_letters + string.digits
        random_message = ''.join(random.choice(characters) for _ in range(30))

        self.input_element.send_keys(random_message)
        self.button.click()

        assert self.message_element.text == random_message

        logger.warning('\ntest_random_messages: Be aware that this test uses randomly generated data\n')

    def test_getting_sys_data(self):       
        platform = sys.platform
        version_info = sys.version_info
        sys_message = f"Platform: {platform} | Version: {version_info}"

        self.input_element.send_keys(sys_message)
        self.button.click()

        assert self.message_element.text == sys_message
    
    def test_using_time(self):       
        self.input_element.send_keys("After typing, I will wait 10 seconds")
        
        time.sleep(10)
        
        self.button.click()

        assert self.message_element.text == "After typing, I will wait 10 seconds"
    
    def test_getting_data_from_csv(self):       
        with open('test_data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                message = f"Player: {row[0]} | Age: {row[1]}"
                self.input_element.send_keys(message)
                self.button.click()
                assert self.message_element.text == message
                self.input_element.clear()       

    def test_manipulating_json(self):       
        json_string = '{"test_name": "test_get_data", "result": "Passed"}'
        data = json.loads(json_string)
        status = f"Test Case: {data['test_name']} | {data['result']}"

        self.input_element.send_keys(status)
        self.button.click()

        assert self.message_element.text == status

    def test_using_locale(self):       
        locale.setlocale(locale.LC_ALL, 'pt_PT.UTF-8')
        product_price = locale.currency(1347.99, symbol=True, grouping=False)
        locale_format = f"Locale Currency: {product_price}"

        self.input_element.send_keys(locale_format)
        self.button.click()

        assert self.message_element.text == locale_format

    def test_using_math(self):       
        cosine = math.cos(180)
        calculation_result = f"The cosine of an 180 degrees angle is approximately: {cosine}"
        
        self.input_element.send_keys(calculation_result)
        self.button.click()
        
        assert self.message_element.text == calculation_result

    def test_using_pickle(self):       
        data_to_pick = {'value': "8412534862354"}

        with open('data.pkl', 'wb') as file:
            pickle.dump(data_to_pick, file)

        with open('data.pkl', 'rb') as file:
            loaded_data = pickle.load(file)

        deserialized_value = loaded_data['value']

        self.input_element.send_keys(deserialized_value)
        self.button.click()

        assert self.message_element.text == deserialized_value

    def test_using_regex(self):       
        regex_pattern = r'\d{3}-\d{2}-\d{4}'  # Example: XXX-XX-XXXX
        value_to_check = '123-45-6789'
        match_result = re.match(regex_pattern, value_to_check)
        matches_regex = f"The result of this validation is {bool(match_result)}"

        self.input_element.send_keys(matches_regex)
        self.button.click()

        assert self.message_element.text == matches_regex

        
if __name__ == '__main__':
    unittest.main()