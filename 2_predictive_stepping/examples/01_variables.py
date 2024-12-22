#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Variables

All the examples so far have not written to or read from program memory.
    They have used values and comparisons directly without saving the results for later.

Variables are how you save and access values in program memory.
Variables are useful, but they also add some complexity to your program,
    this is when the debugger becomes most useful!

You will know you have understood this file when you can:
    1. Predict which line will execute next and how it will change program state
    2. Step forward in the program in the debugger
    3. Check your prediction, correcting your understanding when you make a mistake
    4. repeat from step 1

"""

# you create a new variable by assign a value to it
name = "D'athaniel"  # prediction: a variable "name" will be created and the value "D'athaniel" assined to it

# you can assign a new value to a variable with the same syntax
name = "Mittens"   # prediction: value of the variable name will change to mittens


# variables can also be assigned the value stored in another variable
# notice!  Variables only store one value at a time, the most recent one
hand_thing = name #prediction: a new variable "hand_thing" will be created, and assined the value mittens

# reassigning the new variable does not change the value stored in the other
hand_thing = "glove"  #prediction: a new value glove will be assigned to hand_thing
# and vice-versa
name = "Poalia" #prediction: name will be assigned a new value called "poalia"

# using a variable without first assigning a value will throw an error
#hey = "toadstool" #predict that an error will occur because the value is empty

#using a variable without first assigning a value will throw an error
hey = "" #prediction: that an error will occur because the value is empty. our prediction was wrong. empty str 
         #is considered a value


print("checking out empty hey") #prediction: it will print and move to the next line

hey =  # prediction: there will be an error because of the empty value
