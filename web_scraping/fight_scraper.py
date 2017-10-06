from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib
import os
os.chdir('/Users/courtneyfergusonlee/ufc_fight_analysis/data')

# Load Fight Info from CSV (created in fight url scraper)
fight_info = pd.read_csv('fight_urls.csv', encoding='utf-8')

# Store urls, locations and titles
fight_urls = fight_info['link'].values.tolist()
fight_titles = fight_info['title'].values.tolist()
fight_locations = fight_info['location'].values.tolist()
fight_dates = fight_info['date'].values.tolist()

# Initialize an empty dataframe
fighter_df = pd.DataFrame(columns=['name', 'kd', 'sig_strikes', 'sig_attempts', 'strikes', 'strike_attempts', 
                                   'takedowns', 'td_attempts', 'sub_attempts', 'pass', 'reversals', 'head', 'head_attempts', 'body', 
                                   'body_attempts','leg', 'leg_attempts', 'distance', 'distance_attempts', 'clinch', 'fight_id',
                                   'clinch_attempts', 'ground', 'ground_attempts', 'win/loss', 'referee', 'round', 'method',
                                   'date', 'location', 'title'])

# Helper function to get the tag text
def nice_text(tag):
    return " ".join(str(tag.get_text()).split())


# Iterate through the fight urls, and pull relevant variables/fields
for i in range(len(fight_urls)):
    if i%10==0 and i!=0:
        print i, fight_urls[i], fight_dates[i]
        break
    
    # Store fight event, location and date
    title = fight_titles[i]
    location = fight_locations[i]
    date = fight_dates[i]
    
    sock = urllib.urlopen(fight_urls[i]) # specific URL for a fight
    fight_html = sock.read()
    fight_soup = bs(fight_html, "lxml")
    trs = fight_soup.find_all('tr') # all the tables in each fight URL
    headers = fight_soup.find_all('i')
    bad_call = 0
    
    # Get the name and win/loss status of each fighter
    person_divs = fight_soup.find_all('div', 
                                  class_="b-fight-details__person")
    names = []
    winloss = []
    
    name_1, name_2 = ["ERROR", "ERROR"]
    winloss_1, winloss_2 = ["ERROR", "ERROR"]

    for person_div in person_divs:
        i_tag = person_div.find('i')
        try:
            winloss.append(nice_text(i_tag))
        except:
            winloss.append('ERROR')
        h3 = person_div.find('h3')
        try:
            names.append(nice_text(h3))
        except:
            names.append('ERROR')

    name_1, name_2 = names
    winloss_1, winloss_2 = winloss
    
    try: 
        referee = str(headers[24].get_text()).split()[1] + ' ' + str(headers[24].get_text()).split()[-1]
    except:
        referee = None
    try:
        rounds = str(headers[18].get_text()).split()[1]
    except:
        rounds = None
    try:
        method = str(headers[17].get_text()).split()[0]
    except:
        method = None
    try:
        tr1 = str(trs[1].get_text()).split()
        # Find the location of the 2nd table tr2 (it varies)
        j = 0
        while j < 10:
            if str(trs[j].get_text()).split()[6] == 'Head':
                #print j+1
                tr2 = str(trs[j+1].get_text()).split()
                break
            j += 1
        #print tr1; #print tr2
        
        # Test for the end of names
        k = 0
        while k < len(tr1):
            try:
                int(tr1[k])
                break
            except:
                k += 1
                continue
        #print k
    except:
        print fight_dates[i] + ' bad call'
        bad_call += 1
        continue


    # Add each fighter's information to the dataframe
    fighter1 = pd.DataFrame({'name': [name_1], 'kd': tr1[k], 'sig_strikes': tr1[k+2],
    'sig_attempts': tr1[k+4], 'strikes': tr1[k+10], 'strike_attempts': tr1[k+12], 'takedowns': tr1[k+16],'td_attempts': tr1[k+18],
    'sub_attempts': tr1[k+24], 'pass': tr1[k+26], 'reversals': tr1[k+28], 'head': tr2[k+8], 'head_attempts': tr2[k+10],
    'body': tr2[k+14], 'body_attempts': tr2[k+16], 'leg': tr2[k+20], 'leg_attempts': tr2[k+22], 'distance': tr2[k+26],
    'distance_attempts': tr2[k+28], 'clinch': tr2[k+32], 'clinch_attempts': tr2[k+34], 'ground': tr2[k+38], 
    'ground_attempts': tr2[k+40], 'win/loss': winloss_1, 'referee': referee, 'round': rounds, 'method': method, 'fight_id': i,
    'date': date, 'location': location, 'title': title})

    fighter2 = pd.DataFrame({'name': [name_2], 'kd': tr1[k+1], 'sig_strikes': tr1[k+5], 
    'sig_attempts': tr1[k+7], 'strikes': tr1[k+13], 'strike_attempts': tr1[k+15], 'takedowns': tr1[k+19],'td_attempts': tr1[k+21],
    'sub_attempts': tr1[k+25], 'pass': tr1[k+27], 'reversals': tr1[k+29], 'head': tr2[k+11], 'head_attempts': tr2[k+13],
    'body': tr2[k+17], 'body_attempts': tr2[k+19], 'leg': tr2[k+23], 'leg_attempts': tr2[k+25], 'distance': tr2[k+29],
    'distance_attempts': tr2[k+31], 'clinch': tr2[k+35], 'clinch_attempts': tr2[k+37], 'ground': tr2[k+41], 
    'ground_attempts': tr2[k+43], 'win/loss': winloss_2, 'referee': referee, 'round': rounds, 'method': method, 'fight_id': i,
    'date': date, 'location': location, 'title': title})
    
    fighter_df = pd.concat([fighter_df, fighter1, fighter2], axis=0, ignore_index=True)
    
fighter_df.to_csv('fights.csv', index=False)