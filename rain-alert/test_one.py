import unittest


class Test_One(unittest.TestCase):

    def test_first(self):
        x=2
        self.assertEqual(2,x,'matched')


    def test_second(self):
        self.assertEqual(3,3)

    def test_third(self):
        self.assertIn('Rajeev','Hello Rajeev Shetty')

    def test_fourth(self):
        self.assertTrue('Rajeev','Rajeev')

if __name__ == '__main__':
    unittest.main()