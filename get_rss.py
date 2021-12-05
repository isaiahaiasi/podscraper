# converts JSON data from webcrawler into a usable XML RSS page

# load <channel> info from file to concatenate
# iterate through JSON object, convert mappable values to subElements

# basic layout:
# xml tag
# rss (lots of attrs)
#   channel
#       title
#       atom:link
#       language
#       copyright
#       image
#           url
#           title
#           link
#       (a whole lot of itunes tags I don't care to list)
#       item (these are the episodes)
#           title
#           link (primitive link)
#           dc:creator
#           description
#           itunes:keywords
#           pubDate (Mon, 29 Nov 2021 16:20:16 +0000)
#           enclosure (url, length?, type)

from sys import argv
import json as JS
import xml.etree.ElementTree as ET
import requests


# this is the function that should be swappable--
# takes a dict & converts it to an xml <item>
def get_item(data):
    item = ET.Element('item')

    ET.SubElement(item, 'title').text = data['title']
    ET.SubElement(item, 'link').text = data['url']
    ET.SubElement(item, 'pubDate').text = data['publishedTime']
    ET.SubElement(
        item, 'description').text = str(data['description'])
    set_enclosure(item, data)
    return item


# creates the audio element
# requires fetching the mp3 head to get the size of the audio file
def set_enclosure(item, data):
    res = requests.head(data['mp3Url'], allow_redirects=True)
    ET.SubElement(item, 'enclosure', {
        'url': str(data['mp3Url']),
        'type': 'audio/mpeg',
        'length': res.headers['content-length']
    })


def write_xml(jsonInputPath, xmlInputPath, outputPath):
    tree = ET.parse(xmlInputPath)
    channel = tree.getroot().find('channel')

    with open(jsonInputPath, "r") as jsf:
        for itemData in JS.load(jsf):
            if itemData is not None:
                channel.append(get_item(itemData))

    tree.write(outputPath)


if __name__ == "__main__":
    # get filenames from command line arguments
    json_input, xml_input, output = argv[1], argv[2], argv[3]
    write_xml(json_input, xml_input, output)
