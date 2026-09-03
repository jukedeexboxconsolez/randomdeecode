# python learning circle for beginners/if you suck at coding
# 1st : the newbie 
print("Hello World ") # print is for printing out text or values in a variable name (without parenthesis for variables)

# 2nd : variables/string variables (string is text "for example")

# String Variables
apple = "🍎"
banana = "🍌"

# Variables With Number/Data Holders In them
value = 10

# additonally you can reassign an existing variable/string variable
value = 20
# However What You Should Keep In Mind Is Every Coding Language (Lua, Python, C, C++, C#) or any other coding language has case sensitivity which i will show an example of in a moment (please read over what is done and the comments above it so you dont find yourself in a confusing loop)
# in the first few variables that have been shown they have unique usernames like apple, banana and value without any sort of upper case tweaking if a variable name gets tweaked a little it would make itself as a new variable e,g (value being renamed to Value) would just create a new one since it was only slightly tweaked the same goes for the string values
# i will also give a more clear example of this in code

Value = 30
value = 40

# Both are different here since because of the fact that as i said again was tweaked (in terms of how the variable name is)
# case sensitvity also plays a huge role in reassigning variables (as evident from what i have showed the same variable would have to stay the same in terms of how the variable name is spelled) 
# # You can also print out what's inside a variable/string variable note that the Variable should exist have the exact name it has like shown underneath (case sensitivity) or like we have explained earlier

print(apple) # prints out 🍎 as the string
print(value) # will print 40
print(Value) # value's twin but it will print out a different one since case sensitivity

# It can feel a bit exhausting to explain case sensitvity To Someone who may not be yet experienced in coding or in other words is new to it but this explanation should tackle most of the issues new coders face
# Additionally You Can Print Out A String Concatenation In Python By Doing This
# however please be aware that this only works for strings and not values
print("My Favorite Fruit " + apple)

# to print a value in concatenation you would do these things

print("favorite number", value) # using a comma
# using an f string  # f goes first when doing it
print(f"My Favorite Number Is {value}")  # make sure to add a parenthesis at the end


# you can also do this
print(apple, banana, value) 

# setting true and false values (same process as what we have explained earlier but in booleans)
# i wont even explain this a second time so please take what we learned and use it as an example for this
# we will also get into conditional statements

IsOkay = True
# note that python operates differently than lua (while similar true and false are instead spelled as True/False Instead of lowercase versions)

# you can also create tables 

username = ["videouser0"]

# example of a username table
# you can also put more than one string in a python table (but it must have each , after that is done until the very last one)
# another example

videoplayer = ["videoplayer1", "videoplayer2", "videoplayer3"] # the very last one doesn't need a , but can include one only the others need it

# we can also print these 

print(videoplayer)
print(username)
print(IsOkay)

## this is part one on python learning we will get more into python learning later for now take these as a way to learn python ^_^