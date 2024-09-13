##Day 2
#Basic Syntax and Data Types: 

#Initialising variables 
number1 = 5 
number2 = 10 
result = number1 + number2 
print(result)

#Data Types
#int, float, str, bool, list, tuple, dict, set

integer_number = 7 
print(integer_number, type(integer_number)) #printing data with its type

floating_number = 7.5 
print(floating_number, type(floating_number))

string_Word = 'Strings'
print(string_Word, type(string_Word))

bool = True
print(bool, type(bool))

list_array = [1,2,3,'a','b','c']
print(list_array, type(list_array))

tuple_array = (1,2,3,'a','b','c')
print(tuple_array, type(tuple_array))

dict_array = {
    'key1' : 'value',
    'key2' : 'value2',
}
print(dict_array, type(dict_array))

set_array = {"apple", "banana", "cherry"}
print(set_array, type(set_array))  

#User input and prints the type of the input 
user_input = input('Enter your Input : ')

#to try first and then use, else make an exception for trial if error
try: 
    int_value = int(user_input)
    print(f'Input is integer : {int_value}')

#if above try has error
except ValueError:
    #trying again 
    try: 
        float_value = float(user_input)
        print(f'Input is float : {float_value}')

    #if try has error then exception
    except ValueError:
        #for case-sensetive converting to all lowercase
        if user_input.lower() in ['true','false']:
            print(f'Input is boolean : {user_input}')
        
        else:
            print(f'Input is string : {user_input}')



