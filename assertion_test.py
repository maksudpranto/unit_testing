import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome(
            executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')
        self.driver.get('https://www.google.com/')
        title = self.driver.title
        print("Title of the Webpage: ", title)

        # self.assertEqual("Google", title, "Webpage Title is Not Same")
        self.assertNotEqual("Google", title, 'Test will be Failed')


if __name__ == '__main__':
    unittest.main()
