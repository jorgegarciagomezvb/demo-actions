import unittest
from resta import restar


class TestRestar(unittest.TestCase):
    def testRestar(self):
        self.assertEqual(restar(3,2),1)
        self.assertEqual(restar(-1,1),-2)
        self.assertEqual(restar(8,10),-2)


if __name__=="__main__":
    unittest.main()