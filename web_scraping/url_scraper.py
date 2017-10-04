from bs4 import BeautifulSoup
import pandas as pd
import urllib
import os
os.chdir('/Users/courtneyfergusonlee/ufc_fight_analysis/data')

# Open the main page with events listed
sock = urllib.urlopen('http://www.fightmetric.com/statistics/events/completed?page=all')
page = sock.read()
soup = BeautifulSoup(page, 'lxml')

# Scrape event URLs from the main page
event_urls = []
event_titles = []
event_dates = []
event_locations = []

trs = soup.find_all('tr')
for tr in trs:
    for link in tr.find_all('a'):
        event_urls.append(link.get('href'))
        event_titles.append(" ".join(str(link.get_text()).split()))
    
    for span in tr.find_all('span'):
        event_dates.append(" ".join(str(span.get_text()).split()))
    
    for td in tr.find_all('td'):
        if len(td['class']) == 2:
            event_locations.append(" ".join(str(td.get_text()).split()))

'''
Small test to ensure urls, titles, dates and locations read properly

print "Event Lengths:"
print "urls:", len(event_urls)
print "titles:", len(event_titles)
print "dates:", len(event_dates)
print "locations:", len(event_locations)

print "Event Data:"
print event_urls[:10]
print event_titles[:10]
print event_dates[:10]
print event_locations[:10]
'''

# Pull Fight URLs, dates and locations from each Event URL
fight_urls = []
count = 0
for event_url, title, date, location in zip(event_urls, event_titles, event_dates, event_locations):
    if count%100==0:
        print event_url, title, date, location
    try:
        sock = urllib.urlopen(event_url)
        event_html = sock.read()
        event_soup = BeautifulSoup(event_html, "lxml")

        tds = event_soup.find_all('td')
        for td in tds:
            for link in td.find_all('a'):
                url = link.get('href')
                url_type = url.split('-')[0][-2:] # Fight vs. Fighter; last 2 letters
                if url_type == 'ht': # use er for fighter, ht for fight
                    #print url
                    fight_urls.append([title, url, date, location])
        
    
    except:
        print "HTTP Error on {}".format(title)
        pass
    count += 1

# Save fight URLs to a csv file
fight_urls = pd.DataFrame(
    data=fight_urls, 
    columns=['title', 'link', 'date', 'location'])
fight_urls.to_csv('fight_urls.csv', index=False)

