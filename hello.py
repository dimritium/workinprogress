import os
import requests,bs4
#f=open('scrapd.text','w+')
url="https://www.skillshare.com/paperfinger/teaching"
res=requests.get(url)
res.raise_for_status()
skills=bs4.BeautifulSoup(res.text,"lxml")

followers=""
followers=skills.select('.number')
nof=followers[0].getText();

print nof

courses=[]
c=[]
s=""
c=skills.select('.title-link a')
for i in c:
	s=str(i.getText().strip())
	courses.append(s)

users=[]
nou=skills.select('.ss-icon-user')
for i in nou:
	s=(i.getText().strip())
	users.append(s)

for i in courses:
	print i

for i in users:
	print i