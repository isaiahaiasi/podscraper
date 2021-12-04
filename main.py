from get_data import get_data
from logging import error
import os
from sys import argv
import math
import requests
import json

from dotenv import load_dotenv
load_dotenv()


# only for 0+
def pad_num(n, len=3):
    if n == 0:
        return '0'*len

    digits = int(math.log10(n))+1
    return '0'*(len-digits) + str(n)


def get_url(num):
    return os.environ.get('POD_URL') + '/' + pad_num(num)


def get_html(podNumber):
    url = get_url(podNumber)
    res = requests.get(url)
    return res.text


def fetch_pod_data(_range):
    dataCollection = []
    for i in _range:
        html = get_html(i)
        data = get_data(html)
        dataCollection.append(data)
    return dataCollection


def serialize_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    lowerRange, upperRange, filename = int(argv[1]), int(argv[2]), argv[3]
    data = fetch_pod_data(range(lowerRange, upperRange))
    serialize_data(data, filename)
