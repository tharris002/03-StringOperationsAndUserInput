txt = "The quick brown fox jumps over the lazy dog."

###############################################################################
# DONE: 1. (1 pt)
#   For the following exercises, you may need to reference the material on 
#   string methods.
#
#   And again, you will reference the string at the top of this file.
#
#   Immediately below this _TODO_, write code that:
#     1. Modifies the string to be in all upper case letters, saves it to a 
#        variable called   upper   and prints its value.
#     2. Modifies the string again to be in all lower case letters, saves it to
#        a variable called   lower   and prints its vale.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
upper = txt.upper()
print(upper)
lower = txt.lower()
print(lower)

###############################################################################
# DONE: 2. (1 pt)
#   Immediately below this _TODO_, write code that:
#     - Replaces the word 'brown' with a different color of your choosing.
#     - Saves the result to a variable name
#     - Prints the value of the variable
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
white = txt.replace ("brown", "white")
print(white)
###############################################################################
# DONE: 3. (2 pts)
#   Immediately below this _TODO_, write code that:
#     - Capitalizes the first letter of each word in the string (HINT: look
#       through the methods resource in the pre-class materials that might be
#       helpful)
#     - Saves the result to a variable name
#     - Prints the value of the variable
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
title = txt.title()
print(title)