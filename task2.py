#список, хранящий списки, состоящие из имени и списка коллекции имеющихся момент
collection=[]
#список, хранящий списки из имени и 1 желаемой монеты
wanted=[]
#множество всех имен
all_names=set()

#функция для работы с файлом с коллекцией монет
def open_coll():
  f=open("collection.txt","r")
  for line in f.readlines():
      line=line[0:-1]
      line=line.split(' : ')
      line[1]=line[1].split(', ')
      collection.append(line)
  f.close()
  for item in collection:
      all_names.add(item[0])

#функция для работы с файлом с монетами, которые коллекционер хочет получить
def open_want():
  f=open("wanted.txt","r")
  for line in f.readlines():
      line=line.split(' : ')
      line[1]=line[1][0:-1]
      wanted.append(line)
  f.close()

#основная функция, определяющая возможность обмена, возвращает строку
def check(participants):
  #проверяем все ли введенные имена содержатся во множестве всех имен
  temp = participants.difference(all_names)
  #если есть имена, не принадлежащие множуству всех имен, возвращаем соответствующую строку
  if len(temp) != 0:
    str="There is no: "
    for item in temp:
      str+=item+', '
    return str
  #если таких элементов не нашлось
  else:
    #множество всех монет, которые хотят получить участники обмена
    want_s = set()
    #множество всех монет участников, доступных для обмена
    collect_s = set()
    #составляем мн-во collect_s
    for item in collection:
      temp = set()
      temp.add(item[0])
      if temp.issubset(participants) == True:
        for items in item[1]:
          collect_s.add(items)
    #составляем мн-во want_s
    for item in wanted:
      temp = set()
      temp.add(item[0])
      if temp.issubset(participants) == True:
        want_s.add(item[1])
    #проверяем все ли элементы want_s входят в collect_s
    if want_s.issubset(collect_s):
      #если да, продолжаем проверку
      #проверяем имеет ли каждый участник обмена хотя бы 1 монету,
      # которую желает получить другой участник,
      # т.е. как минимум 1 монета должна входить в want_s
      for item in collection:
        if set(item[0]).issubset(participants):
          if set(item[1]).isdisjoint(want_s):
            #если у участника ни одна монета не принадлежит want_s
            #обмен не возможен
            return "The exchange is impossible!"
      return "The exchange is possible."
    else:
      return "The exchange is impossible!"

def main():
  open_coll()
  open_want()
  print("Enter the participants or exit:")
  aa=input()
  while(aa!="exit"):
      participants=set(aa.split(' '))
      print(check(participants))
      print("Enter the participants or exit:")
      aa = input()

main()