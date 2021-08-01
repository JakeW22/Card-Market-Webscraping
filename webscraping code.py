from bs4 import BeautifulSoup, element
import mechanicalsoup
import mechanicalsoup.stateful_browser
from urllib.request import urlopen
import requests
import time
import re

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

browser.follow_link("12700830")

# Checking if link works:
#print(browser.url)
#print(browser.page)
#browser.launch_browser()

page = browser.page


href_links = ["/en/Magic/Cards/Bloodstained-Mire",
"/en/Magic/Cards/Divest",
"/en/Magic/Cards/Lake-of-the-Dead", 
"/en/Magic/Cards/Mind-Rake",
"/en/Magic/Cards/Polluted-Delta", 
"/en/Magic/Cards/Ravens-Crime", 
"/en/Magic/Cards/Ancient-Tomb",
"/en/Magic/Cards/Ophiomancer",
"/en/Magic/Products/Singles/Legends/Chains-of-Mephistopheles", 
"/en/Magic/Products/Singles/Modern-Horizons-2-Extras/Grief",
"/en/Magic/Products/Singles/Urzas-Saga/Yawgmoth-s-Will",
"/en/Magic/Products/Singles/Weatherlight/Null-Rod"]

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
user_link = "/en/Magic/Users/"
pattern = re.compile("<.*?>")
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
    
    for reputation in new_page:
        new_page.find("div", class_="table-body")
        reputation = new_page.find_all(attrs={"data-original-title": pattern})
        output_reputation = [x["data-original-title"] for x in reputation]
    
    for price in new_page:
        new_page.find("div", class_="table-body")
        price = new_page.find_all("span", attrs="font-weight-bold color-primary small text-right text-nowrap")
        output_price = [x["font-weight-bold color-primary small text-right text-nowrap"] for x in price]
        #output_price = 
    #print(output_quality)
    #print(output_reputation)
    print(output_price)    
    #print(seller.text)
    #for new_page_link in all_text:
    #    link_count += 1
        
    #print(link_count)
    time.sleep(3)


# Changing from Stateful_Browser to Beautiful Soup Object:

#output1 = [x["data-original-title"] for x in excellent_condition]
#    print(output1)
#    good_condition = new_page.find_all(attrs={"data-original-title" : "Good"})
#    output2 = [x["data-original-title"] for x in good_condition]
#    print(output2)
#    nm_condition = new_page.find_all(attrs={"data-original-title" : "Near Mint"})
#    output3 = [x["data-original-title"] for x in nm_condition]
#    print(output3)

# Trying to get the text of the link for seller:
#for seller in new_page.find("div", class_="table-body"):
#        seller = new_page.find("a")
#        print(''.join(seller.find_all(text=True)))

#'<span class="font-weight-bold color-primary small text-right text-nowrap">29,95 €</span>"'
