import unittest
from unittest import mock

from homework.task1 import FileConverter


class TestCaseTask1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.name = 'random.txt'
        cls.csv_file = 'homework/tests/files/test.csv'
        cls.expected = [{'first_name': 'John', 'last_name': 'Doe'}]

    def test_init(self):
        converter = FileConverter(self.name)
        self.assertEqual(self.name, converter.filename)

    def test_error(self):
        converter = FileConverter(self.name)
        with self.assertRaises(Exception) as asrt:
            converter._error()
        self.assertEqual(str(asrt.exception), 'Not supported type')

    def test_read_csv(self):
        converter = FileConverter(self.csv_file)
        self.assertEqual(list(converter._read_csv()), self.expected)

    def test_read_csv_called(self):
        with mock.patch.object(FileConverter, '_read_csv') as my_read_csv:
            converter = FileConverter(self.csv_file)
            converter.read('csv')
            self.assertTrue(my_read_csv.called)

    def test_write_csv_called(self):
        with mock.patch.object(FileConverter, '_write_csv') as my_write_csv:
            converter = FileConverter(self.csv_file)
            converter.write([{'a': '1'}], 'csv')
            self.assertTrue(my_write_csv.called)
        converter.write([{'a': '1', 'b': '2'}], 'csv')
        with open(self.csv_file + '.csv', 'r') as file:
            data = file.read()

        self.assertEqual(data, 'a,b\n1,2\n')
