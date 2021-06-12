import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest  # Skipping this Test
    def test_search(self):
        print("This is Search Test")

    @unittest.skip("I am skipping this Method Due to It is not yet ready")
    def test_advanced_search(self):
        print("This is Advanced Search Method")

    @unittest.skipIf(1 == 2, "This is Not Skipped as 1 and 2 not Equal")
    def test_prepaid_recharge(self):
        print("This is Prepaid Recharge Method")

    def test_postpaid_recharge(self):
        print("This is Post Paid Recharge Method")

    def test_loginby_gmail(self):
        print("This is Login by Email")

    def test_loginby_twitter(self):
        print("This is Login By Twitter")


if __name__ == "__main__":
    unittest.main()
