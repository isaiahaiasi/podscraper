from logging import error
import os
from sys import argv
import math
import requests
import json
from bs4 import BeautifulSoup

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


def get_urls():
    return [get_url(i) for i in range(491)]


def get_html(podNumber):
    url = get_url(podNumber)
    res = requests.get(url)
    return res.text


def try_get(op, bs, default=None):
    try:
        return op(bs)
    except BaseException as err:
        print(err)
        return default


def get_tags(bs):
    return [t.text for t in bs.find('section', class_="tags").find_all('a')]


def get_timejumps(bs):
    return [[li.a.attrs['href'], li.text] for li in
            bs.find('div', class_='time-jumps').find_all('li')]


def get_links(bs):
    return [[li.a.attrs['href'], li.text] for li in
            bs.find('section', id='links').find_all('li')]


def get_guests(bs):
    return [t.text for t in bs.find('section', id='guests').find_all('h3')]


def get_data(html):
    bs = BeautifulSoup(html, 'html.parser')

    # redundant, but allows for nice separation
    try:
        podNumber = int(bs.title.text.split(":")[0])
    except BaseException as err:
        print(err)
        return None

    print(podNumber, '...')

    return {
        'episodeNumber': podNumber,
        'url': get_url(podNumber),
        'canonical': bs.find("meta", property="og:url").attrs['content'],
        'mp3Url': bs.audio.attrs['src'],
        'title': bs.find(id="show-title").h1.text.strip(),
        'publishedTime': bs.find("meta", property="article:published_time").attrs['content'],
        'description': bs.find('div', class_='apply-typography').text.strip(),
        'tags': try_get(get_tags, bs, []),
        'guests': try_get(get_guests, bs, []),
        'links': try_get(get_links, bs, []),
        'timeJumps': try_get(get_timejumps, bs, [])
    }


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


# TODO: download mp3s...


if __name__ == "__main__":
    lowerRange, upperRange, filename = int(argv[1]), int(argv[2]), argv[3]
    data = fetch_pod_data(range(lowerRange, upperRange))
    serialize_data(data, filename)
