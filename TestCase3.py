import unittest


def setUpModule():
    print("This is SetUp Module")


def tearDownModule():
    print("This is TearDown Module")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is Executed Before Every Methods")

    @classmethod
    def tearDown(self):
        print("This is Executed After Every Methods")

    @classmethod
    def setUpClass(cls):
        print("This is Run only One Time BEFORE Executing Methods")

    @classmethod
    def tearDownClass(cls):
        print("This is Run only One Time AFTER Executing Methods")

    def test_search(self):
        print("This is Search Test")

    def test_advanced_search(self):
        print("This is Advanced Search Test")

    def test_prepaid_recharge(self):
        print("This is Prepaid Recharge Test")

    def test_postpaid_recharge(self):
        print("This is Post Paid Recharge Test")


if __name__ == '__main__':
    unittest.main()
