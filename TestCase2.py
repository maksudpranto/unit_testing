import unittest
from selenium import webdriver


class SearchEnginesTest(unittest.TestCase):
    def test_google_search(self):
        self.driver = webdriver.Chrome(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')
        self.driver.get('https://www.google.com/')
        print("Title of the Page is: ", self.driver.title)
        self.driver.close()

    def test_bing_search(self):
        self.driver = webdriver.Chrome(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')
        self.driver.get('https://www.bing.com/')
        print("Title of the Pages is: ", self.driver.title)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
