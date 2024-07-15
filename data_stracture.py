# auto ={
#     "auto1":{
#         'brend':'chevrolet',
#         'yil': 2023,
#         'speed': 100,
#         'repaired_date':[2019, 2022, 2023]
#     },
#     "auto2":{
#         'brend': 'chevrolet',
#         'yil': 2020,
#         'speed': 200,
#         'repaired_date': [2015, 2020]
#     }
# }
# auto['auto2']['repaired_date'] .append(2023)
# print(auto)                                         (2023 sonini qowib qoyadi (repaired iciga))


# print( auto.pop('auto1'))
# print(auto)



#homework   2-misol


# dictionery = {'a': 100, 'b': 200, 'x': 300, 'y': 200}

# key = input ('kalit so\'z kiriting:')

# if key in dictionery.keys():
#     print('bu so\'z allaqachon lu\'gatimizda bor')
# else:
#     value = input ('qiymat liriting :')
#     dictionery[key] = value   


# print(dictionery)    







#homework    1-misol


# dictionery = {0: 10, 1: 20}

# a_dict.update({'0':'10', '1': '20', '2': '30'})

# print(a_dict)







#homework 3-misol


# d1 = {'a' : 100, 'b': 200}
# d2 = {'x' : 300, 'y': 200}
# d1.update(d2)
# print(d1)



#homework 4-miso




# Peoples={
#     'Javohir':20,
#     'Sanjar':25,
#     'Jamshid':27
# }
# ismlar = list(Peoples.keys())
# yoshlar = list(Peoples.values())

# result = f"Ism    Yosh\n{ismlar[0]}  {yoshlar[0]}\n{ismlar[1]}  {yoshlar[0]}\n{ismlar[2]}  {yoshlar[0]}\n{ismlar[3]}  {yoshlar[0]}\n{ismlar[4]}"

# print(result)




#homework 5-misol



# a = {
#     'first' : 1,
#     'second' :None,
#     'third' : 3
# }
# kalitlar = list(a.keys())
# if a[kalitlar[0]] == None:
#     a.pop(kalitlar[0])
# if a[kalitlar[1]] == None:
#     a.pop(kalitlar[1])
# if a[kalitlar[2]] == None:
#     a.pop(kalitlar[2])

# print(a)




#homework 7-misol


# my_set = {'apple', 'banana', 'cherry', 'orange'}

# input_data = input("Ma'lumot kiriting: ")

# if input_data in my_set:
#     my_set.remove(input_data)
#     print(f"{input_data} o'chirildi")
# else:
#     print("Not Found")


#homework 8-misol


# sn1 = {1, 2, 3, 4, 5}
# sn2 = {4, 5, 6, 7, 8}

# farq = sn1.difference(sn2)
# print(farq)



#homework 10-miso



# students = {
#  'Theodore': 19,
#  'Roxanne': 22,
#  'Mathew': 21,
#  'Betty': 20
# }
# ismlar =list(students.keys())
# yoshlar = list(students.values())

# eng_kichkina = min(yoshlar)
# eng_kottasi = max(yoshlar)

# eng_kichkina_index =yoshlar.index(eng_kichkina)
# eng_kottasi_index = yoshlar.index(eng_kottasi)
# print(ismlar[eng_kottasi_index],ismlar[eng_kichkina_index])



#homework 13-misol


# students = [
#     {'student_id': 1, 'name': 'Jean Castro', 'class':'V'},
#     {'student_id': 2, 'name': 'Lula Powell', 'class':'V'},
#     {'student_id': 3, 'name':'Brian Howell','class':'VI'},
# ]

# key = input("Kalit so'zni kiriting: ")
# value = input("Qiymatni kiriting: ")

# found = any(student.get(key) == value for student in students)

# print(found)


#homework 12-misol


# l1 = ['a', 'b', 'c', 'd', 'e', 'f']
# l2 = [1, 2, 3, 4, 5]

# min_len = min(len(l1), len(l2))
# l1 = l1[:min_len]
# l2 = l2[:min_len]

# result_dict = dict(zip(l1, l2))

# print(result_dict)

#dars






# a = ["apple", "banana", "cherry"]
# for x in a:
#     print(x)







# a= ['apple', 'banana', 'cherry',]
# for i,j in enumerate(a):
#     print(i,j)





# matn= 'python is the best'
# for i in matn:
#     print(i)





# a = ['apple', 'banana','cherry']
# for i in range(len(a)):
#     print(a[i])
 





# for i in range(2,30, 4):
#     print(i)



# a = ['apple','banana','cherry']
# b = ['red','blue','white']
# for i in a:
#     for j in b:
#         print(j,i)





# b = ['apple','banana','cherry']
# for i in b:
#     for j in i:
#         print(j)

     
    


# b = ['apple','banana','cherry']
# for i in b:
#     print(i)
#     if i == 'banana':
#         break




# b = ['apple','banana','cherry']
# for i in b:
#     if i == 'banana':
#         print(i)
#         break



#homevork 2-misol


# n = 6 # i + j = 5
# # 3 , 5, 7, 9
# a = 3
# for i in range(1, n): 
#     for j in range(1, n): 
#         if i + j >= a:
#             print('', end='')
#         else:
#             print("*", end='')
#     a += 2
#     print("\n")



#homevork 1-misol


# divisible_by_5_and_7 = []

# for num in range(1500, 2701):
#     if num % 5 == 0 and num % 7 == 0:
#         divisible_by_5_and_7.append(num)

# print(divisible_by_5_and_7)



#homevork 4-misol


# numbers = []

# for num in range(7):
#     if num != 3 and num != 6:
#         numbers.append(num)

# print(numbers)

  




#homevork 8-misol


# number = int(input("Raqamni kiriting: "))

# for i in range(1, number + 1):
#     print(str(i) * i)



#homevork 9-misol



# for i in range(7):
#     for j in range(7):
#         if i == 0 or i == 6 or i + j == 6:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()







 #homevork 10-misol




# for i in range(7):
#     for j in range(7):
#         if i == 0 or j == 3:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()







#dars  1-misol


# a = []
# if not bool(a):
#     print('bow')
# else:
#     print('bow emas')



#dars 9-misol 2-yecim


# for i in range(7):
#     for j in range(7):
#         if i in [0,6] or i + j == 5:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")            




#dars 5-misol



# row = 3
# column = 4
# result = []

# for i in range(row):
#     a = []
#     for j in range (column):
#         a.append(i*j)
#     result.append(a)

# print(result)    



#dars  while

# i = 1
# while i <= 5:
#     print(i)
#     i+=1



#dars hard 1misol



# import random
# kampyuter_oylagan_son = random.randrange(1,11)
# urinishlar_soni = 0
# print('Kampyuter son oyladi siz uni topishingiz kerak!!!')

# biz_oylagan_son = int(input('Kampyuter oylagan sonni kiriting:'))

# while biz_oylagan_son != kampyuter_oylagan_son:
#     urinishlar_soni += 1
#     print('San oylagan son xato qaytadan urinib kor:')
#     biz_oylagan_son = int(input('kampyuter oylagan sonni kiriting:'))
# else:
#     print(f'Tabriklaymiz siz kampyuter oylagan sonni topdingiz,{kampyuter_oylagan_son},urinishlar_soni: {urinishlar_soni},')    


    #dars hard 2-misol



# import random
# kampyuter_oylagan_son = random.randrange(1,11)
# urinishlar_soni = 0
# print('son kiriting kampyuter uni topsin!!!')

# kampyuter_oylagan_son = int(input('biz_oylagan_son:'))

# while kampyuter_oylagan_son != 'biz_oylagan_son':
#     urinishlar_soni += 1
#     print('kampyuter topgan son xato:')
#     kampyuter_oylagan_son = int(input(''))
# else:
#     print(f'siz oylagan sonni kampyuter topdi,{biz_oylagan_son},urinishlar_soni: {urinishlar_soni},')    




# homevork 3-misol



# son = int(input("Iltimos, biror bir butun son kiriting: "))
# yigindi = sum(i for i in range(2, son+1, 2))

# print(f"1 dan {son} gacha bo'lgan barcha juft sonlarning yig'indisi: {yigindi}")

















#homevork 4-misol



# def tubmi(son):
#     if son <= 1:
#         return False
#     if son <= 3:
#         return True
#     if son % 2 == 0 or son % 3 == 0:
#         return False
#     i = 5
#     while i * i <= son:
#         if son % i == 0 or son % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# son = int(input("Iltimos, biror bir butun son kiriting: "))

# natija = tubmi(son)

# print(f"{son} tub sonmi? {natija}")


#homevork 5-misol



# import math

# son = int(input("Iltimos, biror bir butun son kiriting: "))

# factorial = math.factorial(son)

# jarayon = '*'.join(str(i) for i in range(1, son+1))

# print(f"{son}! = {jarayon} = {factorial}")





















#homevork 6-misol




# matn = input("Iltimos, biror bir matn kiriting: ")
# teskari_matn = ""
# for belgi in matn:
#     teskari_matn = belgi + teskari_matn

# print(f"Teskari tartibda matn: {teskari_matn}")




#homevork begin 1-misol



# son = 1

# while son <= 10:
#     print(son)
#     son += 1


#homevork begin 2-misol



# son = int(input("Iltimos, biror bir raqam kiriting: "))

# yigindi = 0
# jarayon = ""

# for i in range(1, son + 1):
#     yigindi += i
#     if i == 1:
#         jarayon += str(i)
#     else:
#         jarayon += "+" + str(i)

# print(f"{jarayon} = {yigindi}")




#homevork begin  3-misol



# while True:

#     son = int(input("Iltimos, biror bir son kiriting: "))
    
#     if son % 2 == 0:
#         print("Juft son kiritildi, tsikl to'xtatildi.")
#         break
#     else:
#         print("Toq son kiritildi, iltimos yana son kiriting.")




#homevork begin 4-misol




# matn = 'While loop'


# indeks = 0
# while indeks < len(matn):
#     print(matn[indeks])
#     indeks += 1




#homevork begin 5-misol




# while True:
#     matn = input("Iltimos, biror bir matn kiriting: ")
    
#     if 'va' in matn:
#         print("bor")
#         break
#     else:
#         print("Matnda 'va' so'zi yo'q, iltimos yana matn kiriting.")





#dars elementry 4-misol



# a,b,c = 4,3,5
# def my_max(a,b):
#     if a>b:
#         return a
#     return b
# result = my_max(my_max(a,b), c)
# print(result)




#dars intermedit 4-misol





# def isPlindrom(a: str):
#     i = 0
#     n = len(a) -1
#     a = a.lower()
#     while i < n:
#         if a[i] != a[n]:
#             return False
#         i += 1
#         n -= 1
#     return True
# print(isPlindrom('Madam'))





#dars 1-misol



# a =[1,2,1]
# def getColcatenation(nums: list):
#     a = nums.copy()
#     nums.extend(a)
#     return nums
# result = getColcatenation([1,2,1])
# print (result)

    

#2-misol



# nums = [1,2,3,4,5,6]
# n = 3
# result = []
# for i in range(n):
#     result.append(nums[[i]])
#     result.append(nums[n + i])
# print(result)
    

#3-misol




# jewels = "aA"
# stones = "aAAbbbb"
# result = 0
# for stones  in jewels:
#     if i in stones:
#         result += stones.count(i)




#4-misol


# s = "Hello World"
# a =s.split()
# print(len(a[-1]))



#homevork 1-mosl leetcode




# def is_power_of_two(n):
#     if n <= 0:
#         return False
#     return (n & (n - 1)) == 0
# n = 1
# print(is_power_of_two(n)) 




#homework 2-misol leedcode





#homework 3-misol leedcode




#homework 4-misol leedcode


# def reverse_string(s):
#     return s[::-1]
# s = ["h", "e", "l", "l", "o"]
# print(reverse_string(s)) 





#dars misollar lambda!!!



# x= lambda a,b:a*b

# print(x(2,3))





#2-misol




# items = [3,2,10,21,23]
# a = list(map(lambda son: son*2,items))
# print(a)




#3-misol



# a = ['python','code','develope','backend']
# def uzunlik(a):
#     return len(a)


# a= list(map(lambda matn: len(matn),a ))




#4-misol


# a = ['python','code','develope','backend']

# def uzunlik(a):
#     if len(a) <= 4:
#         return 0
#     return len(a)

# print()

#5-misol


# matn= ['python','code','develope','backend']

# a = lambda matn: 0 if len(matn) <= 4 else len(matn)
# result = list(map(a,matn))



#6-misol



# y = [44,32,12,54,32,21]

# (def juftmi(son):
#     if son % 2 == 0:
#         return True
#     return False)



#7-misol



# s =['Python',True, 10, 20, False, None]

# (def butun_son(son):
#     if type(s):
#         return True
#     return False)






# a = lambda element: True if type(element) == int else False

# result = list(filter(a, s))

# print(result)



#8-misol reduce!!!!




# from functools import reduce
# result = reduce(lambda x, y: x + y, range(1,101))
# print(result)




#homework 1-misol


# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]

# result = list(map(lambda x, y, z: x + y + z, a, b, c))

# print(result)


#homework 2-misol


# color = ['Red', 'Blue', 'Black', 'White', 'Pink']

# result = list(map(list, color))

# print(result) 
 
#homework 3-misol


# chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o','U', 'a'}
# a = lambda x: (x.upper(), x.lower())
# result = set(map(a, chars))
# print(result)
 


#homework 6-misol


# nums1 = [1,2,3,4,5,6,7,8]
# nums2 = [2,2,3,1,2,6,7,9]

# result = list(map(lambda x,y: x == y, nums1, nums2))

# print(result.count(True))