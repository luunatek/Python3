# Python3
Summary: Functions and Conditionals

    Define a function:

    def cube_volume(a):
        return a * a * a

    Write a conditional block:

    message = "hello there"
     
    if "hello" in message:
        print("hi")
    else:
        print("I don't understand")

    Write a conditional block of multiple conditions:

    message = "hello there"
     
    if "hello" in message:
        print("hi")
    elif "hi" in message:
        print("hi")
    elif "hey" in message:
        print("hi")
    else:
        print("I don't understand")

    Use the and operator to check if both conditions are True at the same time:

    x = 1
    y = 1
     
    if x == 1 and y==1:
        print("Yes")
    else:
        print("No")

Output is Yes since both x and y are 1.

    Use the or operator to check if at least one condition is True:

    x = 1
    y = 2
     
    if x == 1 or y==2:
        print("Yes")
    else:
        print("No")

Output is Yes since x is 1.

    Check if a value is of a certain type with:

    isinstance("abc", str)
    isinstance([1, 2, 3], list)

or

    type("abc") == str
    type([1, 2, 3]) == lst

    Course content
    Overview
    Q&A
    Notes
    Announcements




In this section you learned that:

    A Python program can get user input via the input function:

    The input function halts the execution of the program and gets text input from the user:

    name = input("Enter your name: ")

    The input function converts any input to a string, but you can convert it back to int or float:

    experience_months = input("Enter your experience in months: ")
    experience_years = int(experience_months) / 12

    You can format strings with (works both on Python 2 and 3):

    name = "Sim"
    experience_years = 1.5
    print("Hi %s, you have %s years of experience." % (name, experience_years))

Output: Hi Sim, you have 1.5 years of experience.

    You can also format strings with (Python 3 only):

    name = "Sim"
    experience_years = 1.5
    print("Hi {}, you have {} years of experience".format(name, experience_years))

Output: Hi Sim, you have 1.5 years of experience.
