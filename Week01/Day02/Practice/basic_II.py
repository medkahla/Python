# # 1
# def countdown(num):
#     liste = []
#     for i in range(num,-1,-1):
#         liste.append(i)
#     return liste
# print(countdown(8))

# # 2
# liste = [5,8]
# def p_r(li):
#     print(li[0])
#     return li[1]
# print(p_r(liste))

# # 3
# liste = [6,5,3,1]
# def f_l(li):
#     return li[0]+len(li)
# print(f_l(liste))

# 4
# liste1 = [9,5,1,3,4,6,7]
# liste2 = [9,7]
# def greater(li):
#     nli = []
#     for i in range(0,len(li)):
#         if li[i]>li[1]:
#             nli.append(li[i])
    
#     if len(nli)>2:        
#         print(len(nli))
#         return nli
#     else:
#         return False
# print(greater(liste1))
# print(greater(liste2))

# 5
def length_and_value(a,b):
    liste = []
    for i in range(0,a):
        liste.append(b)
    return liste

print(length_and_value(8,8))