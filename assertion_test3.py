import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')
        # self.driver.get('https://www.google.com/')
        # self.assertIsNone(self.driver)
        self.assertIsNotNone(self.driver)


if __name__ == '__main__':
    unittest.main()
