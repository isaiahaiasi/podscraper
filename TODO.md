# TODO
basically all I want is to make a table for the pod data & a folder full of mp3s

- [x] get links to each podcast episode page (pretty sure site/###/ works--just needs leading 0s)
- [x] for each podcast episode page, grab the data I want
    - at least the mp3 url
    - might also want meta data to construct an rss feed.
    - in that case, compare w current rss & try to find equivalents in the html
      - title
      - description
      - guests
      - not sure about timestamps!
- [x] serialize data to avoid repeatedly hitting the actual website
- [ ] find missing episodes that could not be found by the non-canonical url (eg, episode 404...)
- [ ] write a script to take the data & turn it into an RSS feed
