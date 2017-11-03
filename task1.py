f=open("birthday.txt","r")
# общая "база"-список из списка с именем и датой рождения
baza=[]

# функция, работающая с чтением файла
# заносит данные с файла в базу
def read_file():
    for line in f.readlines():
        if (line[-1] == '\n'):
            line = line[:-1]
        line = line.split(' : ')
        baza.append(line)
    f.close()

# функция, добавляющая новые данные
def add():
    print("Enter name and day of birthday\n(name : dd.mm.yyyy)")
    line = input()
    # проверка на правильность ввода данных
    if ' : ' in line:
        line = line.split(' : ')
        # проверка на правильность ввода данных о дне рождении
        if len(line[1])==10 and int(line[1][0:2])<=31 and int(line[1][3:5])<=12 and line[1][2]=='.' and line[1][5]=='.':
            # если человек с таким именем уже занесен в базу
            for item in baza:
                if line[0]==item[0]:
                    return "Error! Already added!"
            baza.append(line)
            return "Successfully added "+line[0]+' : '+line[1]
        else:
            print("Error! Wrong format of birthday, try again")
            add()
    else:
        print("Error! Wrong format string, try again")
        add()

# функция, удаляющая данные
def delete():
    # проверка на пустоту базы
    if (len(baza) == 0):
        return "Database is empty!"
    else:
        print("Enter name")
        name = input()
        for item in baza:
            if item[0] == name:
                baza.remove(item)
                return "Successfully deleted "+ item[0]+' : '+item[1]
        # если человека с таким именем нет
        return "There is no "+name+ " in database!"

# функция, изменяющая данные
def change():
    # проверка на пустоту базы
    if (len(baza) == 0):
        return "Database is empty!"
    else:
        print("Enter name")
        name = input()
        # ищем в базе данные с таким именем
        for item in baza:
            if item[0] == name:
                # если нашли
                test=False
                while(test==False):
                    print("Change name or birthday?")
                    temp = input()
                    if (temp == "name"):
                        print("Enter new name")
                        name = input()
                        item[0] = name
                        test=True
                    if (temp == "birthday"):
                        test_b=False
                        print("Enter new birthday\n(dd.mm.yyy)")
                        while test_b==False:
                            birthday = input()
                            # проверяем на правильнность ввода данных о дне рождении
                            if len(birthday) == 10 and int(birthday[0:2]) < 31 and int(birthday[3:5]) < 12 and birthday[2] == '.' and birthday[5] == '.':
                                item[1] = birthday
                                test_b=True
                                test=True
                            else:
                                print("Error! Wrong format of birthday, try again")
                                print("Enter new birthday\n(dd.mm.yyy)")
                    if (test==False):
                        print("Error! Wrong command!")
                return "Successfully changed to "+item[0]+' : '+item[1]
        return "There is no "+name+ " in database!"

# функция, вычисляющая возраст
def age():
    # проверка на пустоту базы
    if (len(baza) == 0):
        return "Database is empty!"
    else:
        print("Enter name")
        name = input()
        for item in baza:
            if item[0] == name:
                from datetime import timedelta, datetime
                # вычисляем нынешнюю дату
                now = datetime.now()
                temp = item[1]
                # переводит строку с датой рождения в формат даты
                birthday = datetime(int(temp[6:10]), int(temp[3:5]), int(temp[0:2]))
                # сравниваем даты, находим разницу в днях
                period = now - birthday
                # вычисляем кол-во целых лет
                return item[0]+" is "+str(period.days // 365)+" years old"
        return "There is no "+ name+ " in database!"

# функция, вычисляющая ближайший день рождения
def next_birthday():
    # проверка на пустоту базы
    if (len(baza) == 0):
        return "Database is empty!"
    else:
        from datetime import timedelta, datetime
        # вычисляем нынешнюю дату
        now = datetime.now()
        # минимальная разница
        min = 365
        next = []
        for item in baza:
            temp = item[1]
            # переводит строку с датой рождения в формат даты
            # при этом год заменяем на текущий
            birthday = datetime(int(now.strftime("%Y")), int(temp[3:5]), int(temp[0:2]))
            # сравниваем разницу
            period = birthday - now
            day = period.days
            # если разница меньше -1 ->день рождение в этом году уже прошло -> прибавляем 365
            if day < -1:
                day = 365 + day
            # сравниваем с минимумом
            if day < min:
                min = day
                next.clear()
                next.append(item)
            else:
                if day == min:
                    next.append(item)
        str=""
        for item in next:
            str+= item[0]+' : '+item[1]+', '
        return str

# функция, находящая людей с днем рождения в определенный день, месяц или год
def birthday():
    # проверка на пустоту базы
    if (len(baza) == 0):
        return "Database is empty!"
    else:
        print("Enter date\n(dd.mm, mm or yyyy)")
        date = input()
        str=''
        if len(date) == 5:
            for item in baza:
                birthday = item[1]
                if (birthday[0:5] == date):
                    str+=item[0]+', '
        if len(date) == 2:
            for item in baza:
                birthday = item[1]
                if (birthday[3:5] == date):
                    str+=item[0]+', '
        if len(date) == 4:
            for item in baza:
                birthday = item[1]
                if (birthday[6:10] == date):
                    str+=item[0]+', '
        if str != '':
            return str
        else:
            return "There is no "+ date+ " date in database!"

#функция, работающая с записью в файл
#заносит данные в файл из базы
def write_file():
    f = open("birthday.txt", "w")
    for item in baza:
        f.write(" : ".join(item) + "\n")
    f.close()

def main():
    functions={'add':add,
              'delete':delete,
              'change':change,
              'age':age,
              'next birthday':next_birthday,
              'birthday':birthday}
    read_file()
    print("Enter add, delete, change, age, next birthday, birthday or exit")
    aa=input()
    while aa!="exit":
        if aa in functions.keys():
            print(functions[aa]())
        else:
            print("Error! Wrong command!")
        print("Enter add, delete, change, age, next birthday, birthday or exit")
        aa = input()
    write_file()

main()