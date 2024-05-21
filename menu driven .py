s_v={}
def create_acc(s_v):
    a=int(input("Enter account ID :"))
    b=float(input("Enter initial amount :"))
    s_v[a]=b
    print("the balance is :",s_v[a])
def deposit_acc(s_v):
    a=int(input("ENTER acount ID :"))
    b=float(input("Enter amount to deposit :"))
    if a in s_v:
        s_v[a]=s_v[a]+b
        print("balance account is :",s_v[a])
    else:
        print("account dosenot exist")
def withdraw_acc(s_v):
    a=int(input("Enter the accoount ID :"))
    b=float(input("enter amout to withdrawal :"))
    if a in s_v and b<=s_v[a]:
        s_v[a]=s_v[a]-b
        print("balance amount is :",s_v[a])
    else:
        print("account doesnot exist ")
def delete_acc(s_v):
    a=int(input("enter the account id :"))
    if a in s_v:
        del s_v[a]
        print("account deleted suscefully")
    else:
        print("account no found")












while True:
    print("\nMENU")
    print("1.Create Account")
    print("2.Deposit Amount")
    print("3.Withdraw Amount")
    print("4.Delete account")
    print("5.exit")
    choice=int(input("enter your choice :"))
    if choice==1:
        create_acc(s_v)
    elif choice==2:
        deposit_acc(s_v)
    elif choice==3:
        withdraw_acc(s_v)
    elif choice==4:
        delete_acc(s_v)
    elif choice==5:
        break
    else:
        print("choice not available ")

    

