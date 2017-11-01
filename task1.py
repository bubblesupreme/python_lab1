f=open("birthday.txt","r")
baza=[]
for line in f.readlines():
    line=line.split(':')
    baza.append(line)
f.close()
print(baza)
print("Enter add, delete, change, age, next birthday, birthday or exit")
aa=input()
while aa!="exit":
    if aa=="add":
        print("Enter name and day of birthday\n(name : dd.mm.yyyy)")
        line=input()
        line += '\n'
        line = line.split(':')
        baza.append(line)
        print(line)
    if aa=="delete":
        print("Enter name")
        name=input()
        name+=' '
        k=False
        for item in baza:
            if item[0]==name:
                baza.remove(item)
                print("Successfully deleted ",item[0],item[1])
                k=True
                break
        if (k==False):
            print("There is no ",name,"in database!")
    if aa=="change":
        print("Enter name")
        name = input()
        name += ' '
        k = False
        for item in baza:
            if item[0] == name:
                print("Change name or birthday?")
                temp=input()
                if(temp=="name"):
                    print("Enter new name")
                    name = input()
                    name += ' '
                    item[0]=name
                if (temp == "birthday"):
                    print("Enter new birthday\n(dd.mm.yyy)")
                    birthday= input()
                    birthday=' '+birthday+'\n'
                    item[1] = birthday
                print("Successfully changed to", item[0], item[1])
                k = True
                break
        if (k==False):
            print("There is no ",name,"in database!")
    if aa=="age":
        print("Enter name")
        name = input()
        name += ' '
        k=False
        for item in baza:
            if item[0] == name:
                from datetime import timedelta, datetime
                now = datetime.now()
                temp=item[1]
                birthday = datetime(int(temp[7:11]),int(temp[4:6]),int(temp[1:3]))
                period = now-birthday
                print (item[0]," is ",period.days//365," years old")
                k = True
                break
        if (k == False):
            print("There is no ", name, "in database!")
    if aa == "next birthday":
        if (len(baza)==0):
            print("Database is empty!")
        else:
             from datetime import timedelta, datetime
             now = datetime.now()
             min=365
             for item in baza:
                temp = item[1]
                next=[]
                birthday = datetime(int(now.strftime("%Y")), int(temp[4:6]), int(temp[1:3]))
                period = birthday - now
                day=period.days
                if day<0:
                    day = 365+day
                if (day)<min:
                    min=day
                    next=item
             print(next[0],':',next[1])
    if aa=="birthday":
        print("Enter date\n(dd.mm, mm or yyyy)")
        date=input()
        k=False
        if len(date)==5:
            for item in baza:
                birthday=item[1]
                if (birthday[1:6]==date):
                    print(item[0])
                    k=True
        if len(date)==2:
            for item in baza:
                birthday=item[1]
                if (birthday[4:6]==date):
                    print(item[0])
                    k = True
        if len(date)==4:
            for item in baza:
                birthday=item[1]
                if (birthday[7:11]==date):
                    print(item[0])
                    k = True
        if k==False:
            print("There is no ", date, "in database!")
    print("Enter add, delete, change, age, next birthday, birthday or exit")
    aa = input()
f=open("birthday.txt","w")
for item in baza:
    f.write(":".join(item))
f.close()
