import unittest
import os
from main import pad_num, get_data


class PaddingTestCase(unittest.TestCase):
    def test_input_0(self):
        self.assertEqual(pad_num(0), "000")

    def test_input_0_extra_padding(self):
        self.assertEqual(pad_num(0, 4), "0000")

    def test_input_10(self):
        self.assertEquals(pad_num(10), "010")


class GetDataTestCase(unittest.TestCase):
    def test_bs4_res(self):
        url = os.environ.get('POD_URL') + '/151'
        self.assertEqual(get_data(url), 'awefaw')
