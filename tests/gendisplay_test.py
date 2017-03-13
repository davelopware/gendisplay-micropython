import unittest
import random
import gendisplay
from gendisplay import GenDisplayMapping
from gendisplay import GenDisplay

class TestGenDisplay(unittest.TestCase):

    def test_construct_defaults(self):
        width = 123
        height = 456
        gd = GenDisplay(width, height)
        self.assertEqual(gd._width, width)
        self.assertEqual(gd._height, height)
        self.assertEqual(len(gd._buffer), width)
        self.assertEqual(len(gd._buffer[0]), height)
        self.assertEqual(len(gd._buffer[width-1]), height)
        self.assertEqual(len(gd._mappings), 0)

    def test_add_mapping(self):
        width = 1
        height = 1
        gd = GenDisplay(width, height)
        self.assertEqual(len(gd._mappings), 0)

        gm = GenDisplayMapping()
        gd.addMapping(gm)
        self.assertEqual(len(gd._mappings), 1)

    def test_get_set_pixel(self):
        width = random.randint(2,10)
        height = random.randint(2,10)
        gd = GenDisplay(width, height)

        for x in range(width):
            for y in range(height):
                self.assertEqual(gd.getPixel(x,y), 0)

        randX = random.randint(0,width-1)
        randY = random.randint(0,height-1)
        gd.setPixel(randX, randY, 1)

        for x in range(width):
            for y in range(height):
                if x == randX and y == randY:
                    self.assertEqual(gd.getPixel(x,y), 1)
                else:
                    self.assertEqual(gd.getPixel(x,y), 0)


if __name__ == '__main__':
    unittest.main()
