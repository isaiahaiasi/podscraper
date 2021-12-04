import os
import math
import requests
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


def get_data(html):
    bs = BeautifulSoup(html, 'html.parser')

    # redundant, but allows for nice separation
    podNumber = int(bs.title.text.split(":")[0])

    return {
        'episodeNumber': podNumber,
        'url': get_url(podNumber),
        'canonical': bs.find("meta", property="og:url").attrs['content'],
        'mp3Url': bs.audio.attrs['src'],
        'title': bs.find(id="show-title").h1.text.strip(),
        'publishedTime': bs.find("meta", property="article:published_time").attrs['content'],
        'description': bs.find('div', class_='apply-typography'),
        'tags': [t.text for t in bs.find('section', class_="tags").find_all('a')],
        'guests': [t.text for t in bs.find('section', id='guests').find_all('h3')],
        'links': [[t.a.attrs['href'], t.text] for t in bs.find('section', id='links').find_all('li')],
        'timeJumps': [[li.a.attrs['href'], li.text] for li in bs.find('div', class_='time-jumps').find_all('li')]
    }

# TODO: call get_html & get_data on range 1:491 (or whatever)

# TODO: store everything together & serialize it somehow
# (convert everything to one big JSON file?)

# TODO: download mp3s...


if __name__ == "__main__":
    print(get_urls())
