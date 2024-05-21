# pi=3.14
# r=int(input("enter the radius :"))
# area=pi*r**2
# print("The the area of the circle is :",area)




# x=5
# y=10 
# print("before swapping x =",x, "and y =",y)
# y,x=x,y
# print("after swapping x =",x  ,"and y =",y)



# n=int(input("Enter the number :"))
# if n%2==0:
#     print("The number is even ",n)
# else:
#     print("The number is odd",n)


# f=float(input("Enter the fahrenheit :"))
# c=(f-32)*5/9
# print("Temperature in celsius :",c)


#calculate factorial using loop

# a=int(input("Enter the number :"))
# b=1
# for i in range (1,a+1):
#     b=b*i
# print(b)






# slicing

# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[]
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# print("The even numbers are :",list2)




# conditional satment 

# a=int(input("Enter a year :"))
# if (a%4==0 and a%100!=0) or (a%400==0) :
#     print(a,"is a leap year")
# else :
#     print(a,"is not a leap year")


# a=0
# b=1
# n=int(input("enter the number :"))
# if n==0:
#     print(a)
# elif n==1:
#     print(a , b)
# while(n>0):
#     for i in range(0,n-2):
#         c=a+b
#         print(c)
#         a=b
#         b=c


# for i in range(1,11):
#     if i==5 or i==4 or i==6 or i==7 :
#         continue
#     print(i)

# list =[1,2,3,4,5,6,7,8,9]
# rev = list[::-1]
# print(rev)

# list = [10,25,45,95,70,1000]
# max = max(list)
# min = min(list)
# print("maximum value is :",max)
# print("minimum vaalue is :",min)


# n=int(input("Enter the number :"))
# if n < 0:
#     print("Negative")
# elif n > 0:
#     print("Positive")
# else :
#     print("zero")

# n=float(input("Enter the mark :"))
# if 90<=n<=100:
#     print("A")
# elif 80<=n<=89:
#     print("B")
# elif 70<=n<=79:
#     print("C")
# elif 60<=n<=69:
#     print("D")
# else:
#     print("F")


# for i in range(0,8):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# for i in"PYTHON":
#     for j in():
#         print("")
#     print()

# a="Python"
# print(a[:2])

# a=input("ENTER THE WORD :")
# for i in range(len(a)):
#     for j in range(i+1):
#         print(a[j],end=" ")
#     print()

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

# for k in range(5):
#     for t in range(4-k):
#         print("*",end="")
#         print(" ",)

# 8th

# for i in range(5):
#     for j in range(5-i):
#         print("*",end=" ")
#     print()


pi=3.14
r=int(input("enter the radius :"))
area=pi*r**2
print("The the area of the circle is :",area)