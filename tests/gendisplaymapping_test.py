import unittest
import gendisplay
from gendisplay import GenDisplayMapping
from gendisplay import GenDisplay

class TestGenDisplayMapping(unittest.TestCase):

    def test_construct_defaults(self):
        gm = GenDisplayMapping()
        self.assertEqual(gm._x, 0)
        self.assertEqual(gm._y, 0)
        self.assertIsNone(gm._width)
        self.assertIsNone(gm._height)

if __name__ == '__main__':
    unittest.main()
