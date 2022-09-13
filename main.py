height = 170
weight = 70
index = height //weight  # индекс массы тела#
print(index)
height = int(input("enter height:"))
weight = int(input("enter weight:"))
print(height, weight,index)  #
#№ 2
time_sec = int(input("enter time:"))
hour = time_sec // 3600
min = time_sec % 3600 // 60
sec = time_sec % 3600 % 60
print(f"{hour:02}:{min:02}:{sec:02}")

#№ 3
n = input("enter number: ")
print(int(n) + int(n + n) + int(n + n + n ))
#№ 4
a = int(input("enter number: ")) # 67588
max = 0
while a > 0:
    surplas = a % 10
    if surplas > max:
        max = surplas
    a //= 10
    break
print("Максимальная цифра:",max)

#№4
profit = int(input("enter прибыль:"))
cost = int(input("enter издержки:"))
ind = profit - cost
if ind < 0:
    print("bad")
if ind > 0:
    print("cool!!")
    rent = profit / cost
    work_man = int(input("enter количество рабоников: "))
    profit_each_work = rent / work_man
    print("прибыль из расчета на одного сотрудника",profit_each_work)

# № 5
a = int(input("enter distance:"))
b = int(input("enter right distance"))
day = 1
while a < b:
      a *= 1.1
      day +=1
print(f"на {day}-й день спортсмен пробежал {b}км")

#lesson 2
#1)
a = ["dog",43,34.8]
for word in a:
    print(type(word))

#2)
li = input("введите несколько слов: ").split()
for i in range(0,len(li) - 1,2):
    li[i],li[i - 1] = li[i - 1],li[i]
print(li)
#3)
d = {"зима":[12,1,2],"весна":[3,4,5],"лето":[6,7,8],"осень":[9,10,11]}
m = int(input("введите номер: "))
for el in d:
    if m in d[el]:
        break
print(m)
#второй вариант
m = int(input("введите номер месяца: "))                           
if (m == 12)or(m <= 2):
    print("зима")
elif(m == 3)or(m <= 5):
    print("весна")
elif(m == 6)or(m <= 8):
    print("лето")
elif(m == 9)or(m <= 11):
    print("осень")
if m<1 or m>12:
    print("погугли сколько месяцев в году")

#4
word = input("введите слова:").split()
for i,el in enumerate(word,1):
    print(i ,el[0:10])
#5
li =[7,5,3,3,2]
n = int(input("enter new score: "))
i = 0
for el in li:
    if n <= el:
        i += 1
li.insert(i,n)
print(li)

        
        



        





    


    













    

        


    





    






















