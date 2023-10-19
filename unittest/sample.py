import unittest

class SampleTestCase(unittest.TestCase):

    def setUp(self):
        # Set up resources for each test method
        self.threshold_value = 10

    def tearDown(self):
        # Clean up resources after each test method is executed
        self.threshold_value = 0

    def test_equal(self):
        self.assertEqual(self.threshold_value, 10)

    def test_not_equal(self):
        self.assertNotEqual(self.threshold_value, 20)

    def test_suite(self):
        # Create a test suite
        suite = unittest.TestSuite()
        suite.addTest(SampleTestCase('test_equal'))
        suite.addTest(SampleTestCase('test_not_equal'))
        return suite

if __name__ == '__main__':
    # Use the TextTestRunner to run the tests
    runner = unittest.TextTestRunner()
    runner.run(SampleTestCase().test_suite())
