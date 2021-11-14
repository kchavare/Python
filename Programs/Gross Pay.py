# import getpass as gt

# Hour = ""
# RPH = 2.75
# grossPay = ""

# Val= isinstance(Hour,str)
# Username= gt.getuser()
# while Val:
#     try:
#         Hour = float(input("Enter the total hours you worked in a day:"))
#         Val = isinstance(Hour,str)
#     except Exception as e:
#         print("Incorrect entry, please enter the hours in number.")
# else:
#     grossPay = Hour * RPH
#     print("Dear {0}, Your earning for a day is ${Pay} ".format(Username,Pay=grossPay))
#     print(f"Dear {Username}, Your earning for a day is ${grossPay:.2f} ")


import getpass as gt

Hour = ""
RPH = 10.50
Grosspay = ""
Overtime = 0
OverTimePay = 0
BasePay = 0
Val=""

Username = gt.getuser()
Val = isinstance(Hour,str)
while Val:
    try:
        Hour = float(input("Enter the total hours you worked in a day:"))
        Val = isinstance(Hour,str)
        if Hour <= 40:
            Grosspay = Hour * RPH
        else:
            Overtime = Hour - 40
            BasePay =  (Hour - Overtime) * RPH
            Grosspay = BasePay + (Overtime * (RPH * 1.5))
    except Exception as e:
        print("Incorrect entry, please enter the hours in number.")
else:  
    print("Dear {0}, Your earning for a day is ${Pay} ".format(Username,Pay=Grosspay))