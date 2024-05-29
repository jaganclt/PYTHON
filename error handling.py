
# def even(n):
#     return n%2==0

# print(even(8))
# try:
#     result=10/-3
# except ZeroDivisionError:
#     print("cannot divide by zero")
# finally:
#     print("this will always excicute")




try:
    l=[1,2,3,4,5,6]
    print(l[0])
except IndexError:
    print("indext out of range")
finally:
    print("jagan")