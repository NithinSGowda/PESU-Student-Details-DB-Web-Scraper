import requests
from bs4 import BeautifulSoup

url = 'https://www.pesuacademy.com/Academy/getStudentClassInfo.php'

srn=2201800001
f = open("2EC.json", "w")
f.write("{\n")
for i in range(0,1000):
    myobj = {'loginId': 'PES'+str(srn)}
    srn=srn+1
    print('Extracting => PES'+str(srn)+' successful.')
    x = requests.post(url, data = myobj)
    html_doc = x.text
    i=0
    soup = BeautifulSoup(html_doc, 'html.parser')
    if((soup.td) and (soup.select('tr > td')[1].get_text(strip=True)!='NA')):
        f.write("\t\"" + soup.find_all('td')[1].text + "\": [{\n")
        f.write("\t\t\"PRN\": \"" + soup.find_all('td')[0].text + "\",\n")
        f.write("\t\t\"SRN\": \"" + soup.find_all('td')[1].text + "\",\n")
        f.write("\t\t\"Name\": \"" + soup.find_all('td')[2].text + "\",\n")
        f.write("\t\t\"Class\": \"" + soup.find_all('td')[3].text + "\",\n")
        f.write("\t\t\"Section\": \"" + soup.find_all('td')[4].text + "\",\n")
        f.write("\t\t\"Cycle\": \"" + soup.find_all('td')[5].text + "\",\n")
        f.write("\t\t\"Department\": \"" + soup.find_all('td')[6].text + "\",\n")
        f.write("\t\t\"Branch\": \"" + soup.find_all('td')[7].text + "\",\n")
        f.write("\t\t\"Campus\": \"" + soup.find_all('td')[8].text + "\"\n")
        f.write("\t}],\n")    
f.write("}")
f.close()


srn=2201900001
f = open("1EC.json", "w")
f.write("{\n")
for i in range(0,1300):
    myobj = {'loginId': 'PES'+str(srn)}
    srn=srn+1
    print('Extracting => PES'+str(srn)+' successful.')
    x = requests.post(url, data = myobj)
    html_doc = x.text
    i=0
    soup = BeautifulSoup(html_doc, 'html.parser')
    if((soup.td) and (soup.select('tr > td')[1].get_text(strip=True)!='NA')):
        f.write("\t\"" + soup.find_all('td')[1].text + "\": [{\n")
        f.write("\t\t\"PRN\": \"" + soup.find_all('td')[0].text + "\",\n")
        f.write("\t\t\"SRN\": \"" + soup.find_all('td')[1].text + "\",\n")
        f.write("\t\t\"Name\": \"" + soup.find_all('td')[2].text + "\",\n")
        f.write("\t\t\"Class\": \"" + soup.find_all('td')[3].text + "\",\n")
        f.write("\t\t\"Section\": \"" + soup.find_all('td')[4].text + "\",\n")
        f.write("\t\t\"Cycle\": \"" + soup.find_all('td')[5].text + "\",\n")
        f.write("\t\t\"Department\": \"" + soup.find_all('td')[6].text + "\",\n")
        f.write("\t\t\"Branch\": \"" + soup.find_all('td')[7].text + "\",\n")
        f.write("\t\t\"Campus\": \"" + soup.find_all('td')[8].text + "\"\n")
        f.write("\t}],\n")    
f.write("}")
f.close()


srn=1201900001
f = open("1RR.json", "w")
f.write("{\n")
for i in range(0,3500):
    myobj = {'loginId': 'PES'+str(srn)}
    srn=srn+1
    print('Extracting => PES'+str(srn)+' successful.')
    x = requests.post(url, data = myobj)
    html_doc = x.text
    i=0
    soup = BeautifulSoup(html_doc, 'html.parser')
    if((soup.td) and (soup.select('tr > td')[1].get_text(strip=True)!='NA')):
        f.write("\t\"" + soup.find_all('td')[1].text + "\": [{\n")
        f.write("\t\t\"PRN\": \"" + soup.find_all('td')[0].text + "\",\n")
        f.write("\t\t\"SRN\": \"" + soup.find_all('td')[1].text + "\",\n")
        f.write("\t\t\"Name\": \"" + soup.find_all('td')[2].text + "\",\n")
        f.write("\t\t\"Class\": \"" + soup.find_all('td')[3].text + "\",\n")
        f.write("\t\t\"Section\": \"" + soup.find_all('td')[4].text + "\",\n")
        f.write("\t\t\"Cycle\": \"" + soup.find_all('td')[5].text + "\",\n")
        f.write("\t\t\"Department\": \"" + soup.find_all('td')[6].text + "\",\n")
        f.write("\t\t\"Branch\": \"" + soup.find_all('td')[7].text + "\",\n")
        f.write("\t\t\"Campus\": \"" + soup.find_all('td')[8].text + "\"\n")
        f.write("\t}],\n")    
f.write("}")
f.close()


srn=1201800001
f = open("2RR.json", "w")
f.write("{\n")
for i in range(0,3500):
    myobj = {'loginId': 'PES'+str(srn)}
    srn=srn+1
    print('Extracting => PES'+str(srn)+' successful.')
    x = requests.post(url, data = myobj)
    html_doc = x.text
    i=0
    soup = BeautifulSoup(html_doc, 'html.parser')
    if((soup.td) and (soup.select('tr > td')[1].get_text(strip=True)!='NA')):
        f.write("\t\"" + soup.find_all('td')[1].text + "\": [{\n")
        f.write("\t\t\"PRN\": \"" + soup.find_all('td')[0].text + "\",\n")
        f.write("\t\t\"SRN\": \"" + soup.find_all('td')[1].text + "\",\n")
        f.write("\t\t\"Name\": \"" + soup.find_all('td')[2].text + "\",\n")
        f.write("\t\t\"Class\": \"" + soup.find_all('td')[3].text + "\",\n")
        f.write("\t\t\"Section\": \"" + soup.find_all('td')[4].text + "\",\n")
        f.write("\t\t\"Cycle\": \"" + soup.find_all('td')[5].text + "\",\n")
        f.write("\t\t\"Department\": \"" + soup.find_all('td')[6].text + "\",\n")
        f.write("\t\t\"Branch\": \"" + soup.find_all('td')[7].text + "\",\n")
        f.write("\t\t\"Campus\": \"" + soup.find_all('td')[8].text + "\"\n")
        f.write("\t}],\n")    
f.write("}")
f.close()


srn=1201700001
f = open("3RR.json", "w")
f.write("{\n")
for i in range(0,3500):
    myobj = {'loginId': 'PES'+str(srn)}
    srn=srn+1
    print('Extracting => PES'+str(srn)+' successful.')
    x = requests.post(url, data = myobj)
    html_doc = x.text
    i=0
    soup = BeautifulSoup(html_doc, 'html.parser')
    if((soup.td) and (soup.select('tr > td')[1].get_text(strip=True)!='NA')):
        f.write("\t\"" + soup.find_all('td')[1].text + "\": [{\n")
        f.write("\t\t\"PRN\": \"" + soup.find_all('td')[0].text + "\",\n")
        f.write("\t\t\"SRN\": \"" + soup.find_all('td')[1].text + "\",\n")
        f.write("\t\t\"Name\": \"" + soup.find_all('td')[2].text + "\",\n")
        f.write("\t\t\"Class\": \"" + soup.find_all('td')[3].text + "\",\n")
        f.write("\t\t\"Section\": \"" + soup.find_all('td')[4].text + "\",\n")
        f.write("\t\t\"Cycle\": \"" + soup.find_all('td')[5].text + "\",\n")
        f.write("\t\t\"Department\": \"" + soup.find_all('td')[6].text + "\",\n")
        f.write("\t\t\"Branch\": \"" + soup.find_all('td')[7].text + "\",\n")
        f.write("\t\t\"Campus\": \"" + soup.find_all('td')[8].text + "\"\n")
        f.write("\t}],\n")    
f.write("}")
f.close()


srn=1201600001
f = open("4RR.json", "w")
f.write("{\n")
for i in range(0,3500):
    myobj = {'loginId': 'PES'+str(srn)}
    srn=srn+1
    print('Extracting => PES'+str(srn)+' successful.')
    x = requests.post(url, data = myobj)
    html_doc = x.text
    i=0
    soup = BeautifulSoup(html_doc, 'html.parser')
    if((soup.td) and (soup.select('tr > td')[1].get_text(strip=True)!='NA')):
        f.write("\t\"" + soup.find_all('td')[1].text + "\": [{\n")
        f.write("\t\t\"PRN\": \"" + soup.find_all('td')[0].text + "\",\n")
        f.write("\t\t\"SRN\": \"" + soup.find_all('td')[1].text + "\",\n")
        f.write("\t\t\"Name\": \"" + soup.find_all('td')[2].text + "\",\n")
        f.write("\t\t\"Class\": \"" + soup.find_all('td')[3].text + "\",\n")
        f.write("\t\t\"Section\": \"" + soup.find_all('td')[4].text + "\",\n")
        f.write("\t\t\"Cycle\": \"" + soup.find_all('td')[5].text + "\",\n")
        f.write("\t\t\"Department\": \"" + soup.find_all('td')[6].text + "\",\n")
        f.write("\t\t\"Branch\": \"" + soup.find_all('td')[7].text + "\",\n")
        f.write("\t\t\"Campus\": \"" + soup.find_all('td')[8].text + "\"\n")
        f.write("\t}],\n")    
f.write("}")
f.close()
