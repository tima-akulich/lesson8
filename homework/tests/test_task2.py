import unittest
import shutil
from homework.task2 import *


class TestCaseTask2(unittest.TestCase):
    test_dir = 'test_dir'
    test_dir_2 = 'test_dir/2'
    frog_dir = 'homework/tests/files'

    @classmethod
    def setUpClass(cls):
        try:
            os.mkdir(cls.test_dir)
            os.mkdir(cls.test_dir_2)
        except FileExistsError:
            pass
        with open(cls.test_dir + '/1.jpg', 'w'), \
             open(cls.test_dir + '/2.jpg', 'w'), \
             open(cls.test_dir_2 + '/4.jpg', 'w'), \
             open(cls.test_dir + '/3.txt', 'w'):
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            shutil.rmtree(cls.test_dir)
            shutil.rmtree(cls.test_dir_2)
        except FileNotFoundError:
            pass

    def test_get_images(self):
        result = sorted(list(get_images(self.test_dir)))
        expected = sorted([self.test_dir + '/1.jpg',
                           self.test_dir + '/2.jpg',
                           self.test_dir_2 + '/4.jpg'
                           ])
        self.assertEqual(result, expected)

    def test_thumbnailer(self):
        thumbnailer = Thumbnailer(self.frog_dir, 100, 100)
        result = sorted(thumbnailer.images)
        expected = sorted([self.frog_dir + '/frog.jpg'])
        self.assertEqual(result, expected)
        names = list(thumbnailer.create_thumbnails())
        self.assertEqual(names, [self.frog_dir + '/frog-thumb.jpg'])
        for name in names:
            os.remove(name)
































