x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


# # I 1
# x[1][0] = 15
# print(x)

# # 2
# print(students[0])
# students[0]["last_name"] = "Bryant"
# print(students[0])

# # 3
# print(sports_directory["soccer"])
# sports_directory["soccer"][0] = "Andres"
# print(sports_directory["soccer"])

# # 4
# print(z)
# z[0]["y"] = 30
# print(z)

# # II
# def iterateDictionary(some_list):
#     for i in range(0,len(some_list)):
#         print(some_list[i])
    

# iterateDictionary(students)

# # III
# def iterateDictionary2(key_name, some_list):
#     for i in range(0,len(some_list)):
#         print(some_list[i][key_name])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# IV
def printInfo(li):
    for i in li:
        print(f" {len(li[i])} {i.upper()} ")
        for j in range(0,len(li[i])):
            print(li[i][j])

printInfo(dojo)