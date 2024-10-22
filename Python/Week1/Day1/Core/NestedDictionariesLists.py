x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# changing the value 10 to 15 in X 

x[1][0]=15

# changing the last name of the student from Jordan to Bryant 
print(students[0])
students[0]["last_name"]="Bryant"
print(students[0])

#In the sports_directory, change 'Messi' to 'Andres'
print (sports_directory)
sports_directory["soccer"][0]="Andres"
print (sports_directory)

#Change the value 20 in z to 30
print(z)
z[0]["y"]=30
print(z)

#Iterate Through a List of Dictionaries
def iterateDictionary(students):
    keys_list1 = list(students[0].keys())
    for i in range (len(keys_list1)):
        print (keys_list1[i])
        print (students[i][f"{keys_list1[i]}"])

    keys_list2 = list(students[1].keys())
    for i in range (len(keys_list2)):
        print (keys_list2[i])
        print (students[i][f"{keys_list2[i]}"])

iterateDictionary(students)