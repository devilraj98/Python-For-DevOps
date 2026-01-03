#First Python code 
''' 
print("Hello, DevOps!")

if True:
    print("This is true!")


#Comments in Python start with the hash symbol (#)
#This is a single-line comment  
# You can also use comments to explain your code
# or to prevent execution when testing code 
# This is a multi-line comment
"""This is a multi-line comment 
"""

# You can use comments to make your code more understandable
# and to leave notes for yourself or other developers
# Happy coding!

#variables and data types in Python
#Variables in Python do not require explicit declaration to reserve memory space.
#The declaration happens automatically when you assign a value to a variable.   
greeting = "Hello, World!"


#Data types examples
name = "DevOps" #string
age = 5 #integer
height = 1.65 #float
is_student = False #boolean

#Rules for naming variables in Python
#1. Variable names must start with a letter (a-z, A-Z) or an underscore (_)
#2. The rest of the variable name can contain letters, numbers (0-9), and underscores (_)
#3. Variable names are case-sensitive (e.g., myVar and myvar are different  variables)
#4. Variable names cannot be a reserved keyword in Python (e.g., if, else, while, for, etc.)    
#5. Variable names should not contain spaces or special characters (e.g., !, @, #, $, %, etc.)
#6. Variable names should be descriptive and meaningful to improve code readability

#Example of valid variable names
user_name = "Alice"
user_age = 25
user_height = 1.75
is_user_student = True  

#Example of invalid variable names  
#123user_name = "Alice"  #Invalid: starts with a number
#user name = "Alice"    #Invalid: contains a space
#user-name = "Alice"    #Invalid: contains a hyphen

#Printing variables
print(greeting)

print(type(user_name))  #Output: <class 'str'>
print(type(user_age))   #Output: <class 'int'>
print(type(user_height))#Output: <class 'float'>
print(type(is_user_student)) #Output: <class 'bool'>

#Input from user
user_input = input("Enter your name: ")
print("your Name is",  user_input)

#Basic arithmetic operations
a = 10  
b = 5

#Addition
sum_result = a + b
print("Sum:", sum_result)  #Output: Sum: 15
#Subtraction
sub_result = a - b
print("Subtraction:", sub_result)  #Output: Subtraction: 5
#Multiplication 
mul_result = a * b
print("Multiplication:", mul_result)  #Output: Multiplication: 50
#Division
div_result = a / b
print("Division:", div_result)  #Output: Division: 2.0  
#Modulus (remainder)
mod_result = a % b  
print("Modulus:", mod_result)  #Output: Modulus: 0  
#Exponentiation
exp_result = a ** b
print("Exponentiation:", exp_result)  #Output: Exponentiation: 100000
#Floor Division
floor_div_result = a // b
print("Floor Division:", floor_div_result)  #Output: Floor Division: 2  
#End of the code

'''

#Conditional statements in Python
#If statement
num = 10
if num > 0:
    print("The number is positive.")  #Output: The number is positive.  

#If-Else statement
cpu_usage = 85

if cpu_usage > 80:
   print("Scale up the servers")
else:
   print("Server is stable as of now")

#If-Elif-Else statement
memory_usage = 70   
if memory_usage > 80:
    print("High memory usage")
elif memory_usage > 50:
    print("Moderate memory usage")
else:
    print("Low memory usage")

#Nested If statement
disk_space = 90 
 # Percentage
if disk_space > 80:
    print("Disk space is high.")
    if disk_space > 90:
        print("Warning: Disk space is critically low!")
    else:
        print("Disk space is moderate.")


# Logical Operators in Python
is_server_up = True 
is_database_connected = False
if is_server_up and is_database_connected:
    print("Server and database are operational.")
elif is_server_up or is_database_connected:
    print("Either server or database is operational.")  
else:
    print("Both server and database are down.")




#excerise 1 Write a script that:Takes environment name Prints:“Production deployment” if env is prod Otherwise “Non-production deployment”

environment = str(input("Write the env name: "))

if environment == "prod":
   print("Env is Prod")
else:
   print("Other env")


#exercise 2 Write a script that: Takes CPU usage as input Prints:“High CPU usage” if usage > 75% Prints:“Moderate CPU usage” if usage is between 50% and 75% Prints:“Low CPU usage” if usage < 50%

