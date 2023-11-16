import unittest
from multiplicacion import multi


class TestMultiplicar(unittest.TestCase):
    def testMultiplicar(self):
        self.assertEqual(multi(3,2),6)
        self.assertEqual(multi(-1,3),-3)
        self.assertEqual(multi(8,3),24)


if __name__=="__main__":
    unittest.main()