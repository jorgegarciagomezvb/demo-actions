import unittest
from division import dividir


class TestSumar(unittest.TestCase):
    def testRestar(self):
        self.assertEqual(dividir(6,2),3)
        self.assertEqual(dividir(15,-5),-3)
        self.assertEqual(dividir(8,10),0.8)


if __name__=="__main__":
    unittest.main()