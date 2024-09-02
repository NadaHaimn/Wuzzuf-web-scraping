import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

jop_title=[]
company_name=[]
location=[]
jop_skill=[]
links =[]
date = []
# salary=[]
# requirement=[]
page_num =0

while True:
    # use requests to fetch the url
    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=navbg%7Cspbg&q=data%20analyst&start={page_num}")


    # save page content/markup
    src = result.content                                                                                            


    # create soup object to parse content
    soup = BeautifulSoup(src,"lxml")

    page_limit = int(soup.find("strong").text)
    if(page_num > page_limit // 15):
        print("Pages ended.")
        break

    # find the elements containing info we need
    # --> jop titles, jop skills , company names , location names
    jop_titles = soup.find_all("h2" , {"class" :"css-m604qf"})# find_all --> lists  {key : values}--> dictionary
    company_names=soup.find_all("a",{"class": "css-17s97q8"})
    locations=soup.find_all("span",{"class":"css-5wys0k"})
    jop_skills=soup.find_all("div",{"class":"css-y4udm8"})
    posted_new = soup.find_all("div" ,{"class" : "css-4c4ojb"})
    posted_old = soup.find_all("div" ,{"class" : "css-do6t5g"})
    posted =[*posted_new , *posted_old]

    # loop over returned lists to extract needed info into other lists
    for i in range(len(jop_titles)):
        jop_title.append(jop_titles[i].text.strip())
        links.append(jop_titles[i].find("a").attrs['href']) #--> to get the attributes
        company_name.append(company_names[i].text.strip())
        location.append(locations[i].text.strip())
        skills = jop_skills[i].text.replace(" · " , " / ").strip()
        jop_skill.append(skills)
        date.append(posted[i].text.strip())
    page_num +=1
    print("page switched")


#inside every page

# for link in links :
#     result = requests.get(f"{link}")
#     src = result.content 
#     soup = BeautifulSoup(src,"lxml")
#     salaries = soup.find("div" , {"class" : "css-1uobp1k"})
#     salary.append((salaries).text.strip())
#     requirements = soup.find("span" , {itemprop : responsibilietes}).ul = .find("ul")
#     requir_text= ""
#     for li in requirments.find_all("li"):
#         requir_text+=li.text+"| " #--> to help us read 
#     requir_text = requir_text[:-2]
#     requirement.append(requir_text)



# create csv file and fill it with values and fetch in page details

file_list =[jop_title, company_name , location , date , jop_skill , links ]
exported = zip_longest(*file_list)
with open("E:\python\Projects\jops wuzzuf.csv" ,"w" , newline='', encoding='UTF8') as myfile:
    wr = csv.writer(myfile) # wr --> object from my csv class
    wr.writerow(["Jop title" , "Company name" , "Location" , "Posted" , "Skills" ,"links" ])
    wr.writerows(exported)
