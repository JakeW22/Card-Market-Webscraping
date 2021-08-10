from os import write
from bs4 import BeautifulSoup, element
import mechanicalsoup
import mechanicalsoup.stateful_browser
from urllib.request import urlopen
import requests
import time
import re
import csv
import pandas as pd

# Create stateful browser:
browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent = 'MyBot/0.1: mysite.example.com/bot_info',
)

# Use browser to open web page:
browser.open("https://www.cardmarket.com/en/Magic")

# Due to complex nature of this web page had to use a find_link method first to find my specific link to the correct login page
# Needed to specify text of the link then assigned that link found to a variable:
login_page = browser.find_link("Login", "Log in")

# Use follow_link to follow the link (login_page) to the login page:
browser.follow_link(login_page)

# Testing to see if it worked
#print(browser.get_url())

# Checking new page
#print(browser.page)

# Confirming using 'find_all' method of bs4 object to see if on correct page:
#print(browser.page.find_all("title"))
# Prints correct title of desired page

form = browser.select_form()

# Printing list of all forms on the page
#print(form.print_summary())

# Now login - looking for 'name' of the forms:
browser["username"] = "JacobWakerley22"
browser["userPassword"] = "F27k!@pK"

# Checking to see if form values were inputed correctly:
#print(form.print_summary())

browser.submit_selected()

# Checking to see if successfully logged in:
print(browser.url)
print("*Puts on shades and folds arms* 'I'm in.'")

# Need to now get into the "Buying" Button and navigate to the "My Wants Button" and enter that url:
browser.follow_link("Wants")

browser.follow_link("12845105")

# Checking if link works:
#print(browser.url)
#print(browser.page)
#browser.launch_browser()

page = browser.page


href_links = ["/en/Magic/Cards/Ancestral-Mask",
"/en/Magic/Cards/Argothian-Enchantress",
"/en/Magic/Cards/Bear-Umbra", 
"/en/Magic/Cards/Darksteel-Mutation",
"/en/Magic/Cards/Exploration", 
"/en/Magic/Cards/Karmic-Justice", 
"/en/Magic/Cards/Mesa-Enchantress",
"/en/Magic/Cards/Nyleas-Colossus",
"/en/Magic/Cards/Nylea-God-of-the-Hunt", 
"/en/Magic/Cards/Privileged-Position",
"/en/Magic/Cards/Serras-Sanctum",
"/en/Magic/Cards/Starfield-Mystic",
"/en/Magic/Cards/Stony-Silence",
"/en/Magic/Cards/Sunpetal-Grove",
"/en/Magic/Cards/Verduran-Enchantress"]

seller_country = "sellerCountry=13"
seller_reputation = "sellerReputation=2"
language = "language=1"
min_condition = "minCondition=4"

href_filter = "?" + str(seller_country) + "&" + str(seller_reputation) + "&" + str(language) + "&" + str(min_condition)


href_link = "/en/Magic/Cards/Bloodstained-Mire"

#print(page.find_all("a", href = href_link))
#print(browser.follow_link(href_link))
#print(browser.url)
condition = ("Near Mint", "Excellent", "Good")
credit = ("Outstanding", "Very good")
user_link = "/en/Magic/Users/"
pattern = re.compile("<.*?>")
#price_list = []
#seller_list = []

loop_num = 0
for links in href_links:
    print(links)
    print(page.find_all("a", href = links)) 
    print(browser.open_relative(links + href_filter))
    print(browser.url)
    new_page = browser.page
    all_text = new_page.find("div", class_="table-body")
    link_count = 0

    for quality in new_page:
        new_page.find("div", class_="table-body")
        quality = new_page.find_all(attrs={"data-original-title" : condition})
        output_quality = [x["data-original-title"] for x in quality]

    user = new_page.find_all("a", href=re.compile(user_link))
    seller_list = []
    for seller_name in user:    
        output_name = seller_name.text
        seller_list.append(output_name)
        #print(output_name)
    
    for reputation in new_page:
        reputation = new_page.find_all(attrs={"data-original-title" : credit})
        output_reputation = [x["data-original-title"] for x in reputation]

    spans =  new_page.find_all("span", class_="font-weight-bold color-primary small text-right text-nowrap")
    price_count = 0
    price_list = []
    for price in spans:
        output_price = price.text
        if (price_count % 2) == 0:
            print("Even", output_price)
            price_list.append(output_price)
        else:
            print("Odd", output_price)
        price_count += 1
        #print(output_price)

    #print(seller_list)
    #print(output_reputation)
    #print(output_quality)
    #print(price_list)

    # Adding names of cards to a list:
    card_names = []
    card_text = new_page.find_all("h1")
    for text in card_text:
        name = str(text.text)

    
    
    with open("Sythis_Wants_List/Magic Card " + name + ".csv", mode="w", encoding="utf-8", newline='') as card_file:
            cardwriter = csv.writer(card_file, quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            cardwriter.writerow(["Seller Name", "Seller Reputation", "Card Quality", "Card Price"])
            for value in range(len(seller_list)):
                try: 
                    cardwriter.writerow([seller_list[value], output_reputation[value], 
                    output_quality[value], price_list[value]])
                except IndexError:
                    pass
    loop_num = loop_num + 1
            #for loop in loop_num:
            #    str(loop + 1)
   
    # Time break between each loop to prevent being locked out from website
    time.sleep(3)

 
