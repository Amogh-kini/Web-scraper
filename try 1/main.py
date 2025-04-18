# pip install beautifulsoup4
# pip install lxml

from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

#========================================================================================================================================================================

d ={'company' : [], 'skills' : [], 'money' : [], 'location' : [], 'time1' : [], 'link' : []}
count1 = 0

#========================================================================================================================================================================

URL1 = 'https://internshala.com/internships/work-from-home-computer-science-internships-in-bangalore/duration-2/stipend-10000/'
URL2 = 'https://internshala.com/internships/work-from-home-computer-science,python-django-internships-in-bangalore/duration-2/stipend-10000/'

fetch = requests.get(URL1).text
soup = BeautifulSoup(fetch, 'lxml')

jobs = soup.find_all('div', class_ = 'internship_meta')

#========================================================================================================================================================================

for job in jobs:

    when = job.find('div', class_="color-labels").span.text
    if 'week' in when:
        break

    count1+=1   

    try : 


        company = job.find('p', class_ = 'company-name').text
        skills = job.find('a', class_ = 'job-title-href').text
        money = job.find('span', class_='stipend').text
        location = job.find('div', class_="row-1-item locations").find('a').text.replace(' ','')
        time1 = job.find_all('div', class_="row-1-item")[1].span.text
        l = job.find('a')
        link = "https://internshala.com/" + l['href']

        print(f"Company : {company.strip()}")
        # print(f"skills : {skills}")
        # print(f"Money : {money}")
        # print(f"Time period : {time1}")
        # print(f"Was posted : {when}")
        # print(f"Location : {location}")
        # print(f"Link : {link}")
        # print("")
        print("")
        
        d['company'].append(company.strip())
        d['skills'].append(skills)
        d['money'].append(money)
        d['location'].append(location)
        d['time1'].append(time1)
        d['link'].append(link)

        time.sleep(5)

    except Exception as e:
        print(f"Error[!] : {e}")     

#========================================================================================================================================================================

print(f"Entered {count1} number of Internships !")

#========================================================================================================================================================================

final_data = pd.DataFrame(data=d)    
final_data.to_csv("Internshala_data.csv")

#========================================================================================================================================================================