marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 23,
    "list" : [1,3,8]
}

# print(marks.items())    #dict_items([('Harry', 100), ('Shubham', 56), ('Rohan', 23), ('list', [1, 3, 8])])
# print(marks.keys())     #dict_keys(['Harry', 'Shubham', 'Rohan', 'list'])
# print(marks.values())   #dict_values([100, 56, 23, [1, 3, 8]])
# marks.update({"Harry" : 99, "Renu" : 100})   
# print(marks)    #{'Harry': 99, 'Shubham': 56, 'Rohan': 23, 'list': [1, 3, 8], 'Renu': 100}  
# marks.get("Shubham")  #56
# print(marks.get("Ritu")) #None
# print(marks.get["Ritu"])    #Returns an error

print(marks.items())    #Returns key value pair
print(marks.keys())     #returns only Keys 
print(marks.values())   #returns only values
print(marks.get("Shu", "ACD"))