###############################################################################
# TODO: 1. (5 pts)
#   Immediately below this _TODO_, write code that:
#     - Asks the user what their name is
#     - Waits for the user to input their name and hit enter
#     - Greets the user in a friendly manner while using the name that they
#       entered **See the note below**
#
#   Note: You could do this by using concatenation like you used in m1, but
#         we are going to use a different approach called f-strings.
#
#   f-strings allow you to insert information into a string at a pre-determined
#   point in the string. You can use an f-string by placing an 'f' in front of
#   your string and {VARIABLE_NAME} where you want to put your variable. So,
#   for example, let's say I have a variable
#       name = John
#   that I want to insert into a string, I would do so like this:
#       name = John
#       print(f"Hello {name}! It's nice to meet you!")
#
#   Then, when I run my code, it would print:
#       Hello John! It's nice to meet you!
#
#   Now do this with your own friendly greeting, but use the name that the user
#   enters as your variable that you will insert.
#
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 2. (5 pt)
#   Now you might be thinking, why didn't we just use concatenation to do this?
#   Isn't it just the same thing?
#
#   Well, what if we have a number (of type int) that we want to include in a
#   string? If copy the line of code below and paste it under this todo and run
#   your code, what happens when it runs this line (which should be after your
#   code from the first todo runs)?
#
#   print("txt" + 5)
#
#   You should have gotten an error saying that you can only concatentate a str
#   with a str. This is where f-strings come in handy!
#
#   Immediately below this _TODO_, write code that:
#     - Adds another prompt for the user asking for their favorite number
#     - Allows the user to type in their favorite number and hit enter
#
#       Now, actually, if we just took that input as is we could use
#       concatenation because the input that the user gives is already a
#       string. However, to illustrate this example, we are going to convert it
#       to an int (integer).
#
#     - So, after the user gives their input, use the same process we used to
#       convert a float to an int in the Session 2 exercises to convert the
#       input from the user.
#     - Then, have your code respond to the user by using their name from
#       before and the number that they gave to say this:
#
#           <NAME>, your favorite number is <NUMBER>. What a great number!
#
#           so, for example,
#
#           John, your favorite number is 7. What a great number!
#
#   Now, this code has a limitation. The user can type anything when asked
#   for their favorite number. They could type 'red' or they could even
#   type out 'seven', and the code would throw an error because it can't
#   convert that to a number. Feel free to try it! We will learn how to avoid
#   this from happening, but we will cover it later.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
