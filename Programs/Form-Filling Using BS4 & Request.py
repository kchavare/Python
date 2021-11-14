from bs4 import BeautifulSoup
import requests

# <URL>Link for job application form
URL="https://docs.google.com/forms/d/e/1FAIpQLSds2Ml8CujBsT1Q2g1857_vXQ5KFWZEaK8fuD-fo9FuYMfLSg/viewform?fbzx=-5334258436672484723"


res=requests.get(URL)
if res.ok:
    soup=BeautifulSoup(res.content,"html5lib")
    tags=soup.findAll("input",attrs={
                                        "name":("entry.1078004677_sentinel","fvv","draftResponse","pageHistory","fbzx")
                                    })

# <Data> Dictionary to store data from excel
    Data = {
                "entry.1781500597":"Karan Chavare",
                "entry.1640447617":"kchavare.1289@gmail.com",
                "entry.297979220":"9049647830",
                "entry.1078004677":"Software Engineer"
            }

    for tag in tags:
        if tag.get('value')==None:
            Data[tag.get('name')]=""
        else:
            Data[tag.get('name')]=str(tag.get('value')).replace("\n","")

    print(Data)

    res1=requests.post("https://docs.google.com/forms/u/0/d/e/1FAIpQLSds2Ml8CujBsT1Q2g1857_vXQ5KFWZEaK8fuD-fo9FuYMfLSg/formResponse",data=Data)
    if res1.ok:
        # soup1=BeautifulSoup(res1.content,"html5lib")
        print("Successfullly Applied")
    else:
        print("Something Went Wrong")
else:
    print('Something Went Wrong')

