import bs4
import requests
import json
import time

import util.database as database
collection = database.collection

def fetch():
    print("# Fetching AH discounts...")
    start_time = time.time() * 1000
    
    index_url = 'http://www.ah.nl/bonus'

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    r = requests.get(index_url, headers=headers)
    soup = bs4.BeautifulSoup(r.text, 'html5lib')

    count = 0

    bonus_products = soup.findAll(attrs={'data-class': 'product'})
    for bonus in bonus_products:
        superdata = {}
        superdata['supermarket'] = 'ah'

        try:
            superdata['url'] = "http://www.ah.nl" + bonus.select('div.detail a')[0].get('href')
        except:
            pass
        try:
            superdata['url'] = "http://www.ah.nl" + bonus.get('href')
        except:
            pass
        superdata['productname'] = bonus.select('div.detail h2')[0].get_text().strip()
        superdata['duration'] = soup.select('div.columns p.header-bar__term')[0].get_text()
        superdata['image'] = bonus.select('div.image img')[0].get('data-original')
        try:
            superdata['amount'] = bonus.select('div.image p.unit')[0].get_text().strip()
        except:
            superdata['amount'] = "Unknown"
        superdata['bonus'] = bonus.select('div.shield')[0].get_text().strip()
        superdata['action_price'] = bonus.select('p.price ins')[0].get_text()
        try:
            superdata['old_price'] = bonus.select('p.price del')[0].get_text()
        except:
            superdata['old_price'] = "Unknown"

        count = count + 1
        collection.insert(superdata)

    seconds = (time.time() * 1000) - start_time
    print("# Done fetching {0} AH discounts in {1}ms.\n".format(count, format(seconds, '.2f')))

def test():
    #will define test here
    print("AH test")
