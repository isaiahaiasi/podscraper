from bs4 import BeautifulSoup


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


def try_get(op, bs, default=None):
    try:
        return op(bs)
    except BaseException as err:
        print(err)
        return default
