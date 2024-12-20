import unittest

from Tests.ControllerTest.RootControllerTest.RootTest import RootControllerCase

if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RootControllerCase))

    unittest.TextTestRunner().run(test_suite)
    unittest.main()
