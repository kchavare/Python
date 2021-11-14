##with open('learning_python.txt') as file_object:
##        for i in range(3):
##                content=file_object.read()
##                print(content)
##                print()
##                file_object.seek(0)

#--------Looping each line in file object---------------

##with open('learning_python.txt') as file_object:
##        for line in file_object:
##                print(line.rstrip())
##        print()

#--------By storing in the list and then working outside the with block---------------
##with open('learning_python.txt','r') as file_object:
##        lines=file_object.readlines()
##for line in lines:
##        if 'operators' in line:
##                line.replace('operators','files & folders')
##                print(line,end='')


#Writing to a file:
##name=input("Enter your name:")
##with open('Guest.txt','a') as file_object:
##        file_object.write(name+'\n')

#Writing to the Guest Book:
##flag=True
##while flag:
##    name=input("Enter your name:")
##    with open('Guest_Book.txt','a') as file_object:
##        file_object.write("Thanks for visiting {}, have a nice day!\n".format(name))
##        print("welcome on board",name)

#-----Error handling value error-------
##while True:
##    number1=input("Enter number 1:")
##    number2=input("Enter number 2:")
##    try:
##        result=int(number1)+int(number2)
##    except ValueError:
##        continue
##    else:
##        print(result)
##        print()


#-----Creating and writing in the two file simultaneously-----
##dogname=['rocky','mocky','jocky']
##catname=['leena','teena','beena']
##with open("cats.txt",'w') as file_object1:
##    with open("dogs.txt",'w') as file_object2:
##        for name in dogname:
##            file_object2.write(name.strip()+"\n")
##    for name1 in catname:
##        file_object1.write(name1.strip()+"\n")


#-----Reading the the file-------
##f=None
##f1=None
##try:
##    try:
##        f=open('cats.txt')
##    except:
##        pass
##        #print("cats.txt file not found")
##    else:
##        content1=f.read()
##        print(content1)
##    try:   
##        f1=open('dogs.txt')
##    except:
##        pass
##        #print("dogs.txt file not found")
##    else:
##        content2=f1.read()
##        print(content2)
##except:
##    print("Both files are not available")
##finally:
##    if f != None:
##        f.close
##    if f1 != None:
##        f1.close
    
#------Counting the no of words in a sentence------
count=0
with open('Points.txt') as file_object:
    for line in file_object.readlines():
        print(line,end='')
        count+=line.lower().count('of')
    print(count)





















        
