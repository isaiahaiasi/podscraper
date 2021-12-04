import unittest
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
        with open("./local_fixtures/pod1.html", "r", encoding="utf-8") as fp:
            data = get_data(fp.read())
            self.assertEqual(data, 'awefaw')


class LoadFixture(unittest.TestCase):
    def test_html_fixture(self):
        f = open("./local_fixtures/pod1.html", "r")
        print(f.read())
