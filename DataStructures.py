#Day 5 Data Structures (LIST, TUPPLES, DICTIONARY )

#LIST
# List is a collection of items which can be of any data type including strings, integers, floats
listFruits = ['apple','mango','banana']
print(listFruits[0]) #use indexing to slice an item from the list

print("Listing all the items from the list : ")
for fruit in listFruits:print(fruit)

#TUPPLE
# Tuple is a collection of items which can be of any data type including strings, integers, floats
tuppleFruits = ('apple','mango','banana')
print(tuppleFruits[0]) #use indexing to slice an item from the tupple
print("Listing all the items from the tupple : ")
for fruit in tuppleFruits:print(fruit)

#DICTIONARY
# Dictionary is a collection of key-value pairs
dictFruits = {'apple':'red','mango':'yellow','banana':'yellow'}
print(dictFruits['apple']) #use key to access the value from the dictionary
print("printing dictionary : ")
for key, value in dictFruits.items():print(key,value) #use items() to access


#Question 1: Create a list of numbers and find the maximum, minimum and average. 

listOfNumbers = input('Enter the number seperated by space : ') #taking space seprated numbers
listOfNumbers = list(map(int,listOfNumbers.split())) #converting into list of numbers
listOfNumbers.sort() #sorting list of numbers 
print(listOfNumbers)
print("Maximum number in the list is: ", listOfNumbers[-1])
print("Minimum number in the list is: ", listOfNumbers[0])
print("Average of the list is: ", sum(listOfNumbers)/len(listOfNumbers))

#Question 2: Write a program that takes a list of names and sorts them alphabetically
names = input("Enter list of names seprated by space: ")
names = list(names.split(" ")) #coverting into list
for i in names: 
    i = i.capitalize() #for universal small and capital letters 
    names.sort() #sorting names 
print(names)  

#Question 3: Create a dictionary with some key-value pairs and write a aprogram to update a value based on user input 
dictionary = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
    }
print(dictionary)
def updateValue(dictionary):
    key = input("Enter the key to update: ")
    value = int(input("Enter the new value: "))
    dictionary[key] = value #updating value based on key
    print(dictionary) 

updateValue(dictionary)  #calling function to update value
