# fruits=["apple","jagan","aswanth","anirudh"]
# # emptylist=[]
# # for x in fruits:
# #     if "n" in x:
# #         emptylist.append(x)
# # print(emptylist)


# newlist=[x for x in fruits if "n" in x]
# print(newlist)


# def nm(a):
#     return a**2

# numbers=[1,2,3,4,5,6,7]
# sqr=[i**2 for i in numbers if i%2==0]
# print(sqr)


# flatten 


# matrix =[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix)
# nw=[]
# for i in matrix:
#     for j in i:
#         nw.append(j)
# print(nw)

# newlist=[j for i in matrix for j in i]
# print(newlist)

# words=["hello","jagan","pytho","is","aswanth"]
# # newword=[i[0] for i in words ]
# # print(newword)
# uw=[i.upper() for i in words if len(i)>5]
# print(uw)

l1=[1,2,3,4,5,6,7,8]
# result=["even" if i%2==0  else "odd" for i in l1]
# print(result)
# result=[i for i in l1 if i%2==0 ]
# print(result)

l2=[10,11,12,13,14]
# print(list(zip(l1,l2)))


# for x,y in zip(l1,l2):
    # print(x*y)


p=[x*y for x,y in zip(l1,l2)]
print(p)