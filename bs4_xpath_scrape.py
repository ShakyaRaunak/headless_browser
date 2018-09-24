from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Title</title></head><body><h2>Heading</h2><p>Hello World</p><div><span>This is a test.</span></div></body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

for string in soup.stripped_strings:
    print(repr(string))

print("--------")

for s in soup.strings:
    # print(s)
    # print(repr(s))

    # print(s.find_parents())

    #    for parent in s.parents:
    #        print(parent.name)

    print([parent.name for parent in s.parents if type(parent.name) == str])
