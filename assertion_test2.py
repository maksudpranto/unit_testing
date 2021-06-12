import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome(
            executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')
        self.driver.get('https://www.google.com/')
        title_of_page = self.driver.title
        print("Title of the Page is: ", title_of_page)

        # self.assertTrue(title_of_page == "Google")  # Expression Become True - So, Test Method will be Passed
        self.assertFalse(title_of_page == "Google123")  # Expression Become False - So, Test Method will be Passed


if __name__ == '__main__':
    unittest.main()
