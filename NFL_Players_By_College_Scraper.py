# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 08:50:07 2020

This program scrapes the ESPN site for the current list of players in the NFL 
organized by the college which they played for.

@author: Nate Z
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import string
import time
import random

table_list = [['Player', 'NFL Team', 'Position','College Team']]

for letter in string.ascii_lowercase:
    
    print(letter) #always good to know how it's going
    
    # URL to format and Open
    url = r"http://www.espn.com/nfl/college/_/letter/{letter}"
    
    html = urlopen(url.format(letter = letter)) #open the URL
    
    soup = BeautifulSoup(html, 'html.parser') #extract
    
    table = soup.find('table')
    
    row_list = table.find_all('tr')
    
    college_team = row_list[0].get_text() #set first college team. Prob not necessary
    
    for row in row_list:
        if len(row) == 1:
            college_team = row.get_text()
            continue
        if row.get_text(";") == 'PLAYER;TEAM;POSITION':
            continue
        temp_row = row.get_text(';').split(';')
        temp_row.append(college_team)
        table_list.append(temp_row)
        
    time.sleep(3+random.random()) #don't want to bother ESPN too much
    
player_df = pd.DataFrame(table_list[1:],columns = table_list[0])
        
player_df.to_csv(r'C:\Users\Nate\.spyder-py3\CFB_Database\NFL_Players_By_College.csv', index = False)    