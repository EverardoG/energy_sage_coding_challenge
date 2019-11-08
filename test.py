import unittest
from function import matchObjects

class TestMatchObjects(unittest.TestCase):

    def test_not_a_collection(self):
        with self.assertRaises(TypeError):
            matchObjects(3,[3])
        with self.assertRaises(TypeError):
            matchObjects([3],3)
        with self.assertRaises(TypeError):
            matchObjects(3,3)

    def test_basic_func(self):
        self.assertEqual(matchObjects([3,4,5],[4,5,6]), [4,5])
        self.assertEqual(matchObjects(set([3,4,5]), set([4,5,6])), [4,5])
        self.assertEqual(matchObjects((3,4,5),(6,7,8)), [])

    def test_empty_collections(self):
        self.assertEqual(matchObjects([],[]), [])

if __name__ == '__main__':
    unittest.main()