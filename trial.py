# a=input("ENTER NAME")
# b=input("ENTER AGE")
# c=input("ENTER YEAR")
# d=input("ENTER PLACE")
# print("Name:",a,"Age:",b,"Year:",c,"Place:",d)


# Swapping

# x=48
# y=5
# print("before swapping x=",x," and y= ",y)
# x,y=y,x
# print("after swapping x=",x," and y= ",y)

#calculate the area of circle

# r=float(input("radius"))
# pi=3.14
# area=pi*r**2
# print(area)

# odd or even

# a=int(input("enter a number"))
# if a%2==0:
#     print(a,"is even")
# else:
#     print(a,"is odd")

#calculate factorial using loop

# a=int(input("enter a number"))
# b=1
# for i in range (1,a+1):
#     b=b*i
# print(b)

#fahrenheit to celcius

# f=int(input("enter value"))
# c=(f-32)*(5/9)
# print(c)

#Assignment if if-else,elif statement 
#1st

# i=int(input("input number"))
# if i<0 :
#     print("i is negative")
# elif i==0 :
#     print("i is equal to zero")
# elif i>0 :
#     print("i is positive")

#3rd

# a=int(input("Enter a year :"))
# if (a%4==0 and a%100!=0) or (a%400==0) :
#     print(a,"is a leap year")
# else:
#     print(a,"is not a leap year")

#4

# a=int(input("enter a number"))
# if a==0:
#     print("neither prime nor composite")
# elif a==1:
#      print("neither prime nor composite")
# else:
#      for i in range(2,a):
#           if a%i==0:
#                print("not prime")
#                break
#      else:
#                print("prime")

#5 vowel orconsonant

# a=input("enter a character:")
# b=a.lower()
# if b=="a" or b=="e" or b=="i" or b=="o" or b=="u":
#     print(a,"is a vowel")
# else:
#     print(a,"is a consonant")



#for loop

#1st

# for i in range(1,11):
#     print(i)


# 2nd

# a=0
# for i in range(1,51):
#     if i%2==0:
#         a=a+i
# print(a)

#3

# a=0
# b=1
# n=int(input("enter  a number "))
# print(a)
# print(b)
# for i in range(0,n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c)

#5

# for a in range(2,100):
#     for i in range(2,a):
#         if a%i==0:
#             break
#     else:
#         print(a)


#while loop

#1st

# a=1
# while a<=10:
#     print(a)
#     a+=1

# 2nd

# a=1
# b=0
# while a<50:
#     if a%2!=0:
#         b=b+a
#         print(b)
#     a+=1
    
#3rd

# a="Anirudh"
# b=""
# i=len(a)-1
# while i>=0:
#     b=b+a[i]
#     i=i-1
# print(b)

#4th

# 5th

# a=1
# while a<100:
#     if a%2==0:
#         print(a)
#     a+=1


# Nested Loop


# for i in range (5):
#     for j in range(i+1):
#         print(i,"seed")


# 2nd

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()
    
# 3rd

# for i in range(4):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# 4th

# for i in range(5):
#     for j in range(1,i+2):
#         print(j,end=" ")
#     print()

# 5th

# a=input()
# for i in range(len(a)):
#     for j in range(i+1):
#         print(a[j],end=" ")
#     print()

# 6th

# for i in range(5):
#     for j in range(4-i):
#         print(" ",end="")
#     print((i+1)*"* ")

# 7th

# for i in range(5):
#     for j in range(4-i):
#         print(" ",end="")
#     print((i+1)*"*")

# 8th

# for i in range(5):
#     for j in range(5-i):
#         print("*",end=" ")
#     print()

#9th


# n=input()
# for i in range(n):
#     if i=0 or i=n:
#         for j in range()


# def jagan(a):
#     print(a)





# jagan(123)
# print("-------------------------------------------------------")
# jagan(234)


# def square(num):
#     b=num**2
#     return b

# a=int(input())
# print(square(a))

def function(n1,n2=20):
        sub=n1-n2
        return sub


# a=function(30)
# print(a)

# a=function(50)
# print(a)

# def func(a,b):
#     print("value of a:",a)
#     print("value of b:",b)

# b=int(input("Enter the value of b:"))
# func(b,a)


# def fact(x):
#         if(x==1):
#             return 1
#         else:
#                return (x*fact(x-1)) 
        

# x=3
# d=fact(x)
# print(d)


fibin0cci

