import unittest


class Test(unittest.TestCase):
    def testName(self):
        # self.assertGreater(100, 10)  # 1st value Should be Greater Than 2nd
        # self.assertGreaterEqual(100, 100)   # 1st Number and 2nd Should be Equal or 1st > 2nd
        # self.assertLess(10, 100)  # 1st Number should Less than 2nd
        self.assertLessEqual(10, 10)


if __name__ == '__main__':
    unittest.main()
