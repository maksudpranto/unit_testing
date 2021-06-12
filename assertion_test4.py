import unittest


class Test(unittest.TestCase):
    def testName(self):
        list_item = {"Python", "Selenium", "Java"}

        # self.assertIn("Python", list_item)  # Verify Python is available in list_item or not
        self.assertNotIn("Pythons", list_item)


if __name__ == "__main__":
    unittest.main()
