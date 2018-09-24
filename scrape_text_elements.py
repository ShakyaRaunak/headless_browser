import requests
import lxml.etree as etree

HTML_PARSE_URL = 'http://pythonecommerce.com/'

parsed_html = """
<html><head><title>Title</title></head><body><h2>Heading</h2><p>Hello World</p><div><span>This is a test.</span></div></body></html>
"""

try:
    pass
    # parsed_html = str(requests.get(HTML_PARSE_URL).content)
except:
    print("Error retrieving html content")

print(parsed_html)
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.fromstring(parsed_html, parser)

# for element in tree.iter():
#    print(element.tag)

# print(tree.xpath("string()"))

texts = tree.xpath("//text()")
print(texts)

_tree = etree.ElementTree(tree)
root_tag = _tree.getroot().tag
# print(root_tag)

output = []
for text in texts:
    parent = text.getparent()
    parentTag = parent.tag
    xPathStr = root_tag + '/' + _tree.getelementpath(parent)

    # print(xPathStr)
    output.append([text, xPathStr])

print(output)
