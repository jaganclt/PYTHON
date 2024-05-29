# sqr=[i**2 for i in range(1,11)]
# print(sqr)

# evn=[i for i in range(1,21) if i%2==0]
# print(evn)

# words=["jagan","athira","aswanth","anirudh"]
# j=[len(i)for i in words]
# print(j)


# words=["jagan","athira","aswanth","anirudh"]
# j=[i.upper() for i in words]
# print(j)

# words=["jagan","athira","aswanth","anirudh"]
# j=[i[0] for i in words]
# print(j)

# evn=[x**2 for x in range(1,11,) if x%2==0]
# print(evn)

# numbr=[i for i in range(1,101) if i%3==0 and i%5==0]
# print(numbr)

# matrix =[[1,2,3],[4,5,6],[7,8,9]]
# flatten_l=[j for i in matrix for j in i]
# print(flatten_l)

a=[]

n = int(input())
for i in range(n):
    sq=i**2
    a.append(sq)


for i in a:
    print (i)