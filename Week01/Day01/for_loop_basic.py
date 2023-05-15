# for x in range(0,101):
#     #print(x)
#     # if x % 5 == 0:
#     #     print(x)
#     if x % 10 == 0:
#         print("Coding Dojo")
#     elif x % 5 == 0:
#         print("Coding")
#     else: print(x)

# sum = 0
# for x in range(0,500001):
#     if x % 2 != 0:
#         sum += x
# print(sum)

# for x in range(2018,0,-4):
#     print(x)

low_num = 1
high_num = 8
mult = 2

li = []
for x in range(low_num, high_num):
    if x % mult == 0:
        li.append(x)
print(li)