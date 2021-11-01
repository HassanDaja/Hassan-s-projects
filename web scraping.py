
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import requests

import shlex
import numpy
job_title=[]
company_name=[]
location=[]
exp=[]
job_date=[]
links=[]
salary=[]
x=0

while x<=10:
    ### get data using fetech
    result = requests.get(f"https://wuzzuf.net/search/jobs/?q=python&a=hpb={x}")
    ### page content
    con = result.content
    soup = BeautifulSoup(con, 'lxml')

    ### finding the content we need
    jobTempletes = soup.find_all( "div", {"class":"css-1o5ybe7 e1581u7e0"})
    job_titles=soup.find_all("h2", {"class":"css-m604qf"})
    company_names=soup.find_all("a", {"class":"css-17s97q8"})
    locations=soup.find_all("span", {"class":"css-5wys0k"})
    exps=soup.find_all("div", {"class":"css-y4udm8"})


    for jopTemplete in jobTempletes:
        if jopTemplete.find("div", {"class":"css-do6t5g"}):
                    date = jopTemplete.find("div", {"class":"css-do6t5g"})
                    dateText = date.text.replace("-","").strip()
                    job_date.append(dateText)
        elif jopTemplete.find("div", {"class":"css-4c4ojb"}):
                    date =  jopTemplete.find("div", {"class":"css-4c4ojb"})
                    dateText = date.text.replace("-","").strip()
                    job_date.append(dateText)






    ### get the info from html link
    for job in job_titles:
        job_title.append(job.text)
        links.append(job.find('a').attrs['href'])
    for comp in company_names:
        company_name.append(comp.text)
    for loc in locations:
        location.append(loc.text)
    for ex in exps:
        exp.append(ex.text)
    x+=1
    print(x)



### craet csv file and fill it with the data
file_list=[job_title,company_name,location,exp,links]
exported=zip_longest(*file_list)
with open("C:/Users/GTX/Desktop/sy/jobs.csv","w") as file:
    wr=csv.writer(file)
    wr.writerow(["Job title","Company Name","Location","experience","Job page","salary"])
    wr.writerows(exported)


