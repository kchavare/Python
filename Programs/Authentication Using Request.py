import requests as req
from bs4 import BeautifulSoup


# UserName=str(input("Enter the Username:"))
# PassWord=str(input("Enter the Password:"))

dtaDict={"__RequestVerificationToken":"",
        "ReturnUrl":"",
        "sid":"0",
        "Email":"skirmishing@atandskc.com",
        "Password":"Qwerty@2021",
        "ConfirmPassword":"Qwerty@2021",
        "UserName":"QaureLiedo",
        "IfSendNewsletter":"false"} # Dictionary to store a username ans password

token=''

URL="https://www.wiseowl.co.uk/account/register?sid=0"
with req.session() as s:
        res=s.get("https://www.wiseowl.co.uk/account/register?sid=0")
        soup=BeautifulSoup(res.content,"html5lib")
        tag=soup.find_all('input',attrs={'name':'__RequestVerificationToken'}) # Gets the collection of all the input tag
        token=tag[0]['value'] # Get the value from value attribute from inputtag
        dtaDict['__RequestVerificationToken']=token
        res1=s.post(URL,data=dtaDict)
        soup1=BeautifulSoup(res1.content,"html5lib")
        print(soup1.title)

#res=req.post(url=URL,data=dtaDict)
# token=''
# if res.ok:
#     soup=BeautifulSoup(res.content,"html5lib")
#     print(soup.prettify())
#     tag=soup.find_all('input',attrs={'name':'__RequestVerificationToken'}) # Gets the collection of all the input tag
#     token=tag[0]['value'] # Get the value from value attribute from inputtag
#     print(token)

#     if token !='':
#             dtaDict['__RequestVerificationToken']=token
#             res=req.post("https://www.wiseowl.co.uk/account/register?sid=0",dtaDict)
#             if res.ok:
#                soup1=BeautifulSoup(res.content,"html5lib")
#                print(soup1)


#     print(tag)
#     print(type(tag))
#     print(dir(tag))

#     print(20 * '#')
    
#     print(tag[0])
#     print(type(tag[0]))
#     print(dir(tag[0]))

