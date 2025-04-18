#pip install bs4.
# Beautiful soup docs
# pip install pandas.
from bs4 import BeautifulSoup 
import os
import pandas as pd

d = {'title' : [], 'price' : [], 'link' : []}
num=0

for file in os.listdir("data"):
    num+=1

    try :
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

        t=soup.find("h2")
        title = t.get_text()

        l = t.find("a") # inside t i.e ("h2").
        link = "https://amazon.in/" + l['href']

        p = soup.find("span", attrs={"class": 'a-price-whole'})
        price = p.get_text()

        print("Name : \n",title,"\n","Link : \n",link,"\n","Price : \n",price)
        print()
        print()

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)

    except Exception as e:
        print(f"Error in file {file}: {e}")   


print(f"===================== {num} number of data Entered  ======================")


# pandas
final_data = pd.DataFrame(data=d)    
final_data.to_csv("Data.csv")