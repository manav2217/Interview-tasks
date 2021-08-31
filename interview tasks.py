''' Simple step pattern '''

# for i in range(1,6):
#     print(i * "*")

# reverse

# for i in range(1,6):
#     print((6-i)* "*")

# merge

# for i in range(1,6):
#     print(i*"*" , (6-i)*"*")

# both up and down

# for i in range(1,6):
#     print(i*"*")
# for i in range(1,6):
#     print((6-i)*"*")

'''step pattern right side'''

'''Print numbers in steps'''
# rows = 6
# for num in range(rows):
#     for j in range(num):
#         print(num , end="")
#     print()

'''inverted'''

# row  = int(input("enter row"))
# num = 0
# for num_in_row in range(row , 0 , -1):
#     num += 1
#     for j in range(1 , i+1):
#         print(num , end="")
#     print('\r')

'''star patterns'''

# row = int(input("Enter the number of rows:"))
# for i in range(0,row):
#     for j in range(1,row-i):
#         print("",end=" ")
#     for j in range(1,(2*i-1)+1):
#         print("*",end="")
#     print("")

'''Fibbonaci series'''

# n = int(input("Enter the number : "))
# n1 , n2 = 0 , 1
# count=0

# if n<=0:
#     print("Enter positive number")
# elif n==0:
#     print("series is",n1)
# else:
#     print("Series is :")
#     while count<n:
#         nth = n1+n2
#         n1=n2
#         n2=nth
#         count+=1
#         print(nth)

'''output tricky'''

# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]
# print(names1 , names2 , names3)


# names2[0] = 'Alice'
# print(names1 , names2 , names3)
# names3[1] = 'Bob'
# print(names1 , names2 , names3)

# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         sum += 1
#     if ls[1] == 'Bob':
#         sum += 10

# print(sum)

'''hello in list'''

# print(list("hello"))

'''average'''

# n = int(input("Enter the number of element : "))
# a = []
# for i in range(0,n):
#     element = int(input("enter the number : "))
#     a.append(element)
#     avg = sum(a)/n

# print(avg)

'''reverse'''

# n = int(input("Enter the number to be reverse"))
# rev = 0
# while(n>0):
#     x = n%10
#     rev = rev*10+x
#     n = n//10
#     print(rev)

# n = int(input("Enter the number"))
# sum = 0
# while(n>0):
#     x = n%10
#     sum = sum+x
#     n=n//10
#     print(sum)

'''palindrom'''

# n = int(input("Enter the number"))
# per = n
# pal = 0
# while(n>0):
#     x = n%10
#     pal = pal*10+x
#     n=n//10

# if per == pal:
#     print(True)
# else:
#     print(False)

'''count numbers'''

# n = int(input("Enter the number"))
# count = 0
# while(n>0):
#     count = count+1
#     n = n//10
# print(count)

'''table'''

# n = int(input("Enter the number :"))
# for i in range(1,11):
#     x = i*n

#     print(n ,"X" ,i ,"=", x)

'''prime'''

# n = int(input("Enter the number"))
# k = 0
# if n == 1:
#     print("please enter a valid number")
# elif n == 0:
#     print("please enter a valid number")
# for i in range(2,n):
#     if n%i == 0:
#         k = 1
#     else:
#         k = k
# if k>0:
#     print(True)
# elif k == 0 :
#     print(False)

'''factorial'''

# n = int(input("enter the number"))
# fact = 1
# if n == 1:
#     print("fact : 1")
# elif n == 0:
#     print("not valid")
# for i in range(1 , n+1):
#     fact = fact*i
# print(fact)

'''seconf largest element'''

# n = int(input("Enter the total number"))
# a = []
# for i in range(n):
#     x = int(input("Enter the element  : "))
#     a.append(x)
# a.sort()
# print("second largest element is" , a[-2])

'''swap first and last number of list'''

# n = int(input("enter the number"))
# a = []
# for i in range(n):
#     x = int(input("Enter the element  : "))
#     a.append(x)
# print(a)
# temp = a[0]
# a[0] = a[-1]
# a[-1] = temp
# print(a)

'''string palindrom'''

# n = str(input("Enter the text"))
# if n == n[::-1]:
#     print(True)
# else:
#     print(False)

'''vovel count'''

# n = str(input("Enter the text"))
# vovel = set("aeiouAEIOU")
# count = 0
# for i in n:
#     if i in vovel:
#         count+=1
# print(count)

'''common latters'''

# n1 = str(input("Enter the text"))
# n2 = str(input("Enter the text"))

# a = list(set(n1)&set(n2))
# print(a)

'''file handling'''

'''create file'''

# f = open("demo.txt" , "x")  #'''only create'''
# f = open("demo.txt" , "a")  #'''create if not exist'''
# f = open("demo.txt" , "w")  #'''create if not exist'''

'''readfile'''

# f = open("demo.txt" , "r")  # "r" is default value
# print(f.read())  # read file in one line
# print(f.readline()) #read line by line


'''write'''

# f = open("demo.txt" , "w")
# f.write("this is new line")
# f.close()  # always close after open file

'''append'''

# f = open("demo.txt" , "a")
# f.write("this is new line")
# f.close()  # always close after open file

'''delete'''

# import os
# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
# else:
#     print("File not exist")

'''armstrong'''

# n = int(input("Enter the number"))
# s= str(n)
# l = len(s)
# count = 0
# temp = n
# while(temp>0):
#     x = temp%10
#     s = pow(x , l)
#     count = count+s
#     temp = temp//10

# if count == n:
#     print(True)
# else:
#     print(False)


'''area of circle'''

# r = int(input("Enter the radius"))
# pi = 3.14
# area = pi*(r*r)
# print(area)

'''prime series'''

# n = int(input("Enter the start number"))
# n1 = int(input("Enter the end number"))

# for i in range(n , n1+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             print(i)

'''nth fibbonaci'''

# def fibbonaci(n):
#     if n<=0:
#         print("not valid input")
#     elif n == 1:
#         return 0
#     elif n == 2 :
#         return 1
#     else:
#         return fibbonaci(n-1)+fibbonaci(n-2)

# print(fibbonaci(10))

'''fibbonaci with search'''

# n = int(input("Enter the max of fibbonaci"))
# s = int(input("Enter the number to be search"))
# search = 0


# def fibonaci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("invalid")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n):
#             c = a+b
#             a = b
#             b = c
#             print(b)
#         return b


# print(fibonaci(n))
# for i in range(fibonaci(n)):
#     if s == i:
#         search = 1
#     else:
#         search = search
# if search == 1:
#     print(True)

'''check for ascii number (unicode value ) using ord() function inbuilt'''

# n = str(input("Enter the element"))
# if len(n) >= 2:
#     print("enter the single character")
# elif len(n) == 1:
#     print("the ascii number is " , ord(n))

'''squar of first n natural number'''

# n = int(input("Enter the number : "))
# count = 0
# for i in range(1 , n+1):
#     x = pow(i,2)
#     count = count+x
# print(count)

'''Find remainder of array multiplication divided by n'''

# n = int(input("enter the array length"))
# mul = 1
# arr = []
# for i in range(n):
#     x = int(input("Enter the array value"))
#     arr.append(x)
# print(arr)
# for i in arr:
#     mul = mul*i
# print(mul%14)

'''swap first and last value'''

# a = [1 , 5 , 4 , 7]
# temp = a[0]
# a[0] = a[-1]
# a[-1] = temp
# print(a)

'''swap element by position'''
# a = [4 , 7 , 8 , 9 , 4 , 5]
# n = int(input("enter the first postition"))
# n2 = int(input("enter the postition to swap"))
# temp = a[n]
# a[n] = a[n2]
# a[n2] = temp
# print(a)

'''clear list'''
# a = [4 , 7 , 8 , 9 , 4 , 5]
# a.clear()
# print(a)

'''remove empty tuple , list in list'''

# a = [4 , 7 , 8 , 9 , 4 , 5 , [] , () , () , [4 , 5 , 8], [4 , 8]]
# a2 = a
# a3 = [ele for ele in a2 if ele!=[]]
# a4= [ele for ele in a2 if ele!=()]
# print("list remove",a3)
# print("tuple remove",a4)

'''count list element'''

# a = [4 , 7 , 8 , 9 , 4 , 5 , [] , [4 , 5 , 8], [4 , 8]]
# print(a.count(4))

'''print duplicate elements'''

# a = [4 , 7 , 8 , 9 , 9 , 8 , 8 , 7 , 12 , 4 , 5 , [] , [4 , 5 , 8], [4 , 8]]
# for i in range(len(a)):
#     k = i+1
#     for j in range(k , len(a)):
#         if a[i] == a[j]:
#             print(a[i])

'''find Cumulative sum of a list'''

# a = [4 , 7 , 8 , 9 , 9 , 8 , 8 , 7 , 12 , 4 , 5 ]
# a2 = []
# sum = 0
# for i in range(len(a)):
#     sum = sum+a[i]
#     a2.append(sum)
# print(a2)

'''Sort the values of first list using second list in Python'''

# x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

# zip_pairs = zip(y , x)

# z = [x for _,  x in sorted(zip_pairs)]
# print(z)

'''timestamp'''

# import time
# import datetime

# string = "12/08/2021"
# print(time.mktime(datetime.datetime.strptime(string , "%d/%m/%Y").timetuple()))

# timestamp = 1628706600.0
# dt_obj = datetime.datetime.fromtimestamp(timestamp)
# print(dt_obj)

'''read word by word in file'''

# with open("demo.txt") as file:
#     for line in file:
#         for word in line.split():
#             print(word)

'''character by charachter'''

# f = open("demo.txt")
# c = f.read()
# for i in c:
#     print(i)

'''add two matrix'''
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# b = [[4, 5, 6],
#      [1, 2, 3],
#      [7, 8, 9]]

# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]

# for i in range(len(a)):
#     for j in range(len(b)):
#         result[i][j] = a[i][j] + b[i][j]

# for r in result:
#     print(r)


'''multiply'''
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# b = [[4, 5, 6],
#      [1, 2, 3],
#      [7, 8, 9]]

# result = [[1, 1, 1],
#           [1, 1, 1],
#           [1, 1, 1]]

# for i in range(len(a)):
#     for j in range(len(b)):
#         result[i][j] = a[i][j] * b[i][j]

# for r in result:
#     print(r)

'''add sub and transpose matrix'''

# import numpy as np
# a = np.array([[1 , 2 , 3],
#              [3, 4, 4]])

# b = np.array([[1, 2, 5],
#              [3, 4, 7]])


# print(np.add(a, b))
# print(np.subtract(a, b))
# print(np.transpose(a))

'''Matrix creation of n*n'''

# n = 4
# a = [list(range(1+i*n , 1+n*(i+1))) for i in range(n)]
# print(a)
# k = 2

'''string is Symmetrical or Palindrome'''

# string = "khokho"
# half = int((len(string)) / 2)

# if len(string) % 2 == 0:
#      firsthalf = string[:half]
#      secondhalf = string[half:]
# else:
#      firsthalf = string[:half]
#      secondhalf = string[half+1:]

# if firsthalf == secondhalf:
#      print("Symmetrical ")
# elif string[::-1] == string:
#      print("palindrom")


'''Reverse words in a given String in Python'''

# s = "geeks quiz practice code"
# a = s.split(" ")
# r = ' '.join(reversed(a))
# print(r)

''' Check if a Substring is Present in a Given String'''

# s = "geeks quiz practice code"
# a = s.find("quizs")
# if a == -1:
#      print("no")
# else:
#      print("yes")

# from math import trunc
# import random
# import string
# import time

# posiblecharachter = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

# n = "abcd"

# attemptthis = ''.join(random.choice(posiblecharachter)for i in range(len(n)))
# attemptnext = ''

# completed = False
# iteration = 0

# while completed == False:
#     print(attemptthis)
#     attemptnext = ''
#     completed = True

#     for i in range(len(n)):
#         if attemptthis[i] != n[i]:
#             completed = False
#             attemptnext += random.choice(posiblecharachter)
#         else:
#             attemptnext += n[i]

#     iteration  += 1
#     attemptthis = attemptnext
#     time.sleep(0.1)

# print(attemptnext)
# print(iteration , "words checked for given word")

'''possible words in one word'''

# from itertools import permutations

# a = "man"
# p = permutations(a)

# d = []

# for i in list(p):
#     if i not in d:
#         d.append(i)
#         print(''.join(i))

'''exec is execute the code in doc string'''

# a = '''print(5)'''
# exec(a)

# list = [1 , 5 , 7]
# tuple = ( 1 , 7)
# list += tuple
# print(list)