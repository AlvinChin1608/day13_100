############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

"""
https://pythontutor.com/visualize.html#mode=edit

Debugging number 1

For i from 1 to 20 and if i reaches 20, then only print
(1,20) will never reach 20 because computer count from 0
change (1,21)
"""

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# ^ reproduce the bug solution
"""
I noticed that whenever it reaches 6, the IndexError: list index out of range put up
also the chosen number is always one index number ahead
solution is to - 1
"""
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # or shifiting down the number (0,5)
# print(dice_imgs[dice_num-1])


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# ^ Play Computer - solution
"""
The 'and' implies that the condition of both year must be true. 
and we need to include the year as well using =
"""
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

    
# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# ^ Fix the Errors - solution
""" 
indentation error, need to define datatype, and else for people before age 18 and f in the print
"""
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")
# else:
#   print(f"You can't drive at age {age}")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# ^ Print is Your Friend - solution
"""
I noticed == instead of =
"""
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# ^ Use a Debugger - solution
"""
The print(b_list) statement is located inside the mutate function. This means it will only print the contents of b_list when the function is called. The output won't be automatically stored or displayed elsewhere in your code.

indentation issue with the append that is responsible for adding the new value in 

https://pythontutor.com/visualize.html#mode=edit
"""

# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,13])

# Challenge 1 bug issue 
"""
# Which year do you want to check?
year = input()

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

I have this error prompt:
"Traceback (most recent call last): TypeError: not all arguments converted during string formatting"

The solution to this error is to use proper string formatting functions such as int() or str() to obtain the desired data type.
"""

# ^ Challenge 1 bug issue - solution
"""
define the year datatype 
year = int(input())
"""

# Challlenge 2 - FizzBuzz
"""
The code needs to print the solution to the FizzBuzz game.

Your program should print each number from 1 to x where x is the input number.

However when the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
"""

# ^ Challlenge 2 - FizzBuzz - Solution
"""
change if to elif
change or to and so both condition are met
last print we do not want to print a list remove the square bracket

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
"""
