##Day 3 CONTROL STRUCTURES: 

##  IF STATEMENTS:
# when if conditions are met true then, code executes.

## ELIF STATEMENTS:
# when user wants to run more if conditions other than if statements.

## ELSE STATEMENTS:
# when none of the conditons are true, so user provides a default output.

# A GUESSING GAME : through if, else and elif statements.
import random 
#randomizing a number between 1 to 10
secret_number = random.randint(1,10) 
guess = None #to store guessed value

while guess != secret_number: # loop will continue until user guesses the number correctly
    guess =int(input("Guess a number between 1 and 10: ")) # asking user to guess a number
    if guess == secret_number: # 
        print("You guessed it!") # 
    elif guess < secret_number: 
        print("TOO LOW") 
    elif guess > secret_number: 
        print("TOO HIGH")
    else:
        print("ENTER A NUMBER : (1-10)")

## FOR STATEMENTS and RANGE FUNCTION:
# used to itterate over a list, dict, tupple, set or can be used in function range().

listing_alphabets = [chr(i) for i in range(ord('a'),ord('z')+1)]
# printing all alphabets from a to z
for i in listing_alphabets:
    print(i,sep=' ',end=' ')

## WHILE LOOP:
# itterates until statement is true.
count = 0 
while count < 5:
    print("Working")
    count+=1
print("Count now is equals to 5.")

## BREAK and CONTINUE STATEMENTS:
#using break
for n in range (2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,"equals",x,"*",n//x)
            break
        else:
            print(n,"is a prime number")

#using continue
for num in range(2,10):
    if num % 2 ==0:
        print("Found an even number",num)
        continue
    print("Found an odd number",num)

#using PASS
while True: pass

##MATCH STATEMENTS: #same as switch 
#  used to match the value of an expression to a series of values.

def http_error(status):
    match status:
        case 400:
            return "BAD REQUEST"
        case 404:
            return "NOT FOUND"
        case 418:
            return "I'm a Teapot"
        case _: #default value
            return "Something's wrong with the internet."