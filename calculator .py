def sum(a,b):
    sum=a+b
    print("The sum of two numbers :",sum)
def sub(a,b):
    sub=a-b
    print("The sub of two numbers :",sub)
def mul(a,b):
    mul=a*b
    print("The multiple of two numbers :",mul)
def div(a,b):
    div=a/b
    print("The division of two numbers :",div)

    
while True:
    print("\nMenu")
    print("1.sum of two numbers")
    print("2.difrence between two numbers")
    print("3.multiple of two numbers")
    print("4.division of two numbers")
    print("5.exit")
    choice=int(input("\nENTER THE CHOICE :"))
    if choice==1:
        print("\nADD")
        a=int(input("Enter first number :"))
        b=int(input("Enter second number :"))
        sum(a,b)
    elif choice==2:
        print("\nSUB")
        a=int(input("Enter first number :"))
        b=int(input("enter second number :"))
        sub(a,b)
    elif choice==3:
        print("\nMULTIPLE")
        a=int(input("Enter first number :"))
        b=int(input("enter second number :"))
        mul(a,b)
    elif choice==4:
        print("\nDIVIDE")
        a=int(input("Enter first number :"))
        b=int(input("enter second number :"))
        div(a,b)
    else:
        break