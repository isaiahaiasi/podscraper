import unittest
from main import pad_num
from get_data import get_data
from local_fixtures.poddata import poddata


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
            self.assertEqual(data['episodeNumber'], poddata['episodeNumber'])
            self.assertEqual(data['url'], poddata['url'])
            self.assertEqual(data['canonical'], poddata['canonical'])
            self.assertEqual(data['mp3Url'], poddata['mp3Url'])
            self.assertEqual(data['title'], poddata['title'])
            self.assertEqual(data['publishedTime'], poddata['publishedTime'])
