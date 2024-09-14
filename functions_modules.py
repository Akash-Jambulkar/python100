##Day 4 Functions & Modules 

#Function def():
#initiating function 
def greet(name):
    print(f"Hello, {name}")

#calling function
greet("John")

##Modules in python: 

#1. Built-in modules
import math
print(math.pi)

#2. External modules
import random
print(random.randint(1, 10))

#3. Custom modules

#creating a custom module
#using the custom module
import module
print(module.add(5, 10))

#Question 1: Write a funtion that takes two numbers and returns their sum. 
def addTwoNumbers():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result = num1 + num2 
    print("Sumission of the two numbers are: ",result)

addTwoNumbers()

#Question 2: Create a function that checks whether a given string is a palindrome:
def palidromeChecker(word):
    reverseWord = word[::-1]
    if word == reverseWord:
        print('Palindrome')
    else:
        print('Not a Palindrome')

palidromeChecker('am')

#Question 3: Import math module and use it to calculate the square root a number 
import math 

number = int(input('Enter a number : '))
squareRoot = math.sqrt(number)
print('Square root of the number is: ', squareRoot)