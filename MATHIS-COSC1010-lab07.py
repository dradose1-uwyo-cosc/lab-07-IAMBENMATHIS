# Benjamin Mathis
# UWYO COSC 1010
# 10/29/24
# Lab 07
# Lab Section: 10
# Sources, people worked with, help given to: Jackson Fetsco, Lab Tech Paige
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

fact = 1
i = 1
active = True
while active:
    print("Enter 'exit' to end the program.\n")

    upper_bound = input("Enter a positive whole integer here: ")
    if upper_bound.lower() == "exit":
        break
    if upper_bound.isdigit():
        print("Good job! You can follow instructions!\n")
        upper_bound = int(upper_bound)
        while i < upper_bound:
            i += 1
            fact = fact * i
        print(f"The result of the factorial based on the given bound is {fact}.\n")
        fact = 1
        i = 1
    else:
        print("You really need to go back to kindergarden. Try Again")
        break



print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

num_sum = 0 
while active:

    num_for_sum = input("Enter the numbers you would like to add, then exit to complete the program: ")
    
    if num_for_sum.lower() == "exit":
        break
    
    if "-" in num_for_sum:
        num_for_sum = num_for_sum.replace("-", " ")
        if num_for_sum.isdigit():
            num_for_sum = int(num_for_sum)
            num_sum = num_sum - num_for_sum
    print(num_for_sum)
    
    if "-" not in num_for_sum:
        if num_for_sum.isdigit():
            num_for_sum = int(num_for_sum)
            num_sum = num_sum + num_for_sum
    
    print(num_sum)
        
    
print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 
number_list = []
math_variable = 0
while active:
    calc_entry = input("Enter a two operand calculation, enter exit to end program: ")
    calc_entry = calc_entry.replace(" ", "")
    
    if calc_entry.lower() == "exit":
        break
    
    if "+" in calc_entry:
        number_list = calc_entry.split("+")
        print(number_list)
        output = 0
        for i in range(len(number_list)):
            if number_list[i].isdigit():
                number_list[i] = int(number_list[i])
                output += number_list[i]
        
    
    if "-" in calc_entry:
        number_list = calc_entry.split("-")
        print(number_list)
        output = 0
        for i in range(len(number_list)):
            if number_list[i].isdigit():
                number_list[i] = int(number_list[i])
        output = number_list[0] - number_list[1] 
        
        
    if "/" in calc_entry:
        number_list = calc_entry.split("/")
        print(number_list)
        output = 0
        for i in range(len(number_list)):
            if number_list[i].isdigit():
                number_list[i] = int(number_list[i])
        output = number_list[0] / number_list[1]
        
    
    if "*" in calc_entry:
        number_list = calc_entry.split("*")
        print(number_list)
        output = 0
        for i in range(len(number_list)):
            if number_list[i].isdigit():
                number_list[i] = int(number_list[i])
        output = number_list[0] * number_list[1]
        

    if "%" in calc_entry:
        number_list = calc_entry.split("%")
        print(number_list)
        output = 0
        for i in range(len(number_list)):
            if number_list[i].isdigit():
                number_list[i] = int(number_list[i])
        output = number_list[0] % number_list[1]
    print(output)



