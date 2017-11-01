f=open("collection.txt","r")
collection=[]
for line in f.readlines():
    line=line[0:-1]
    line=line.split(' : ')
    line[1]=line[1].split(', ')
    collection.append(line)
f.close()
f=open("wanted.txt","r")
wanted=[]
for line in f.readlines():
    line=line.split(' : ')
    line[1]=line[1][0:-1]
    wanted.append(line)
f.close()
print(collection)
all_names=set()
for item in collection:
    all_names.add(item[0])
print("Enter the participants or exit:")
aa=input()
while(aa!="exit"):
    participants=set(aa.split(' '))

    print(participants)
    temp=participants.difference(all_names)
    if len(temp)!=0:
        print("There is no ",temp)
    else:
        want_s=set()
        collect_s=set()
        test=False
        for item in collection:
            temp=set()
            temp.add(item[0])
            if temp.issubset(participants)==True:
                for items in item[1]:
                    collect_s.add(items)
    #print("collect",collect_s)
        for item in wanted:
            temp = set()
            temp.add(item[0])
            if temp.issubset(participants) == True:
                want_s.add(item[1])
    #print(want_s)
        if want_s.issubset(collect_s):
            for item in collection:
                if set(item[0]).issubset(participants):
                    if set(item[1]).isdisjoint(want_s):
                        test=True
                        print("The exchange is impossible!")
                        break
            if test==False:
                print("The exchange is possible.")
        else:
            print("The exchange is impossible!")
    print("Enter the participants or exit:")
    aa = input()
