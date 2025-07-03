
# # x =5
# # y = "5"
# # print(x + int(y)) #10



# # cities = ["Delhi", "Paris", "Tokyo", "Paris"]
# # position = cities.index("Paris")
# # print(position)   #1



# colors = ["red", "green", " blue"]
# colors.clear()
# print(colors)   #[]



# numbers = [100, 200, 300 ,400]
# removed = numbers.pop(2)
# print(removed)  # 300



# animals = ['cat', 'dog', 'lion','dog']
# animals.remove('dog')
# print(animals)  #['cat', 'lion', 'dog']


fruits = ['apple', 'banana']
extras = ['cherry','date']
fruits.extend(extras)
print(fruits)   #['apple', 'banana', 'cherry', 'date']


x = [1,2,3]
x.insert(2,3)
print(x)    #[1, 2, 3, 3]



x = "12345"
print(x[1:-1])  # 234


x = "Data"
y = x * 2
print(y)    #DataData


nums = [10, 20, 30]
nums[1] = " "
print(nums)     #[10, ' ', 30]



words = ["Python" , "is", "fun"]
result = "".join(words)
print(result)   #Pythonisfun


