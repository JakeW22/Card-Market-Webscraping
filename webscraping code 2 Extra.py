from os import link
from bs4 import BeautifulSoup, element
import mechanicalsoup
import mechanicalsoup.stateful_browser
from urllib.request import urlopen
import requests
import time

# Create stateful browser:
browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent = 'MyBot/0.1: mysite.example.com/bot_info',
)

# Use browser to open web page:
browser.open("https://www.cardmarket.com/en/Magic/Cards/Bloodstained-Mire?sellerCountry=13&sellerReputation=2&language=1&minCondition=4")

new_page = browser.page
all_text = new_page.find("div", class_="table-body")

input_tag = new_page.find_all(attrs={"data-original-title" : "Excellent"})

output = [x["data-original-title"] for x in input_tag]

print(output)