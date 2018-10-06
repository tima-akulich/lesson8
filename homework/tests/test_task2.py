import unittest
import os
import shutil
from homework.task2 import *


class TestCaseTask2(unittest.TestCase):
    test_dir = 'test_dir'
    test_dir_2 = 'test_dir/2'

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

    def tearDown(self):
        try:
            shutil.rmtree(self.test_dir)
            shutil.rmtree(self.test_dir_2)
        except FileNotFoundError:
            pass

    def test_ok(self):
        self.assertTrue(True)

    def test_get_images(self):
        result = sorted(list(get_images(self.test_dir)))
        expected = sorted([self.test_dir + '/1.jpg',
                           self.test_dir + '/2.jpg',
                           self.test_dir_2 + '/4.jpg'
                           ])
        self.assertEqual(result, expected)
