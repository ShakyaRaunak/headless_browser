"""
Develop Python 3 script that utilizes either Chrome Headless or Phantomjs headless browser to return a list of only
nodes that contain text along with the font size of each node. Each element in the output list should contain the
following data:
* Node XPath Full Selector: example: /html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div[3]/div[1]/span/span
* Font size: example: 12 px, 1.25rem...etc

"""

# https://duo.com/decipher/driving-headless-chrome-with-python

import os
from timeit import timeit

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def test_headless_browser(browser_type):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe' if \
        browser_type == 'CHROME' else 'C:\\Users\\rauna\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'

    driver = webdriver.Chrome(executable_path=os.path.abspath("assets\\chromedriver"), chrome_options=chrome_options)
    driver.get("http://www.duo.com")

    magnifying_glass = driver.find_element_by_id("js-open-icon")
    if magnifying_glass.is_displayed():
        magnifying_glass.click()
    else:
        menu_button = driver.find_element_by_css_selector(".menu-trigger.local")
        menu_button.click()

    search_field = driver.find_element_by_id("site-search")
    search_field.clear()
    search_field.send_keys("Olabode")
    search_field.send_keys(Keys.RETURN)
    # print(driver.page_source)

    assert "Don't @ Me: Hunting Twitter Bots at Scale | Duo Security" in driver.page_source
    driver.close()


print("first: ", timeit('test_headless_browser("CHROME")', number=1, globals=globals()))
print("second: ", timeit('test_headless_browser("CHROME_CANARY")', number=1, globals=globals()))
