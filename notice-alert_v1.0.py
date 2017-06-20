#-------------------------------------------------------------------------#
#                       notice-alert                                      #
#   Find and automatically download all new notices from College Website. #
#                  KNIT Sultanpur @shvm-7397                              #
#-------------------------------------------------------------------------#

import bs4
from bs4 import BeautifulSoup
import urllib.request

static_url = r'http://knit.ac.in/'
urlObj = urllib.request.urlopen(static_url)
soup = BeautifulSoup(urlObj.read(), 'html.parser')
tag = soup.find('ul', style = 'list-style-type: none; margin:0')
Notice, i = False, 0
for each in tag :
    if each.name == 'li' :
        data = each.contents
        for every in each.contents :
            if every.name == 'img' :
                i += 1
                if not Notice :
                    print('New Notices found. (Will be automatically downloaded)')
                Notice = True
                print(data[0].string)
                down_link = 'http://knit.ac.in/' + data[0]['href']
                recieve = urllib.request.urlretrieve(down_link, r"D:\\Notice" + str(i) +".pdf")
                
if not Notice :
    print('No New Notice')
print("That's all for today!")
