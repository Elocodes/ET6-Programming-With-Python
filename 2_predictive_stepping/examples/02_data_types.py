#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Data Types

"Types" are different ways to represent data in a program.
Different types are useful for modeling different aspects of the world in your program.

We will start with only 4 types: string, integer, float, boolean.
You can use type() to print the type of a value.

"""

# Strings: store and work with text data
a_string = "Pine trees make pinecones." # prediction: a variable "a_string" will be created and the text in the value assigned to it 
a_string = ""  # an empty string is still a string #prediction: varibale "a_string" will be replaced with an empty str

# Integer: represent whole numbers
an_integer = 1  #prediction: variable "an_integer" will be created and the value 1 assigned to it
an_integer = 0  #prediction: variable "an_integer" will be assigned 0
an_integer = -12  #prediction: variable "an_integer" will be assigned -12

# Float: represents decimal numbers
a_float = 1.0 #prediction: variable "a_float" will be created and the value 1.0 assigned to it
a_float = 0.1 #prediction: variable "a_float" will be assigned 0.1
a_float = -1.2  #prediction: variable "a_float" will be assigned -1.2

# Boolean: useful for "yes"/"no" situations
a_boolean = True   #prediction: variable "a_boolean" will be created and the value True assigned to it
a_boolean = False  #prediction: variable "a_boolean" will be assigned False

# --- isinstance() : test the type of a value ---

# passing
pass_check_string = isinstance(a_string, str)  #prediction: a variable called "pass_check_string" will be created and it will be assigned True
pass_check_integer = isinstance(an_integer, int)  #prediction: a variable called "pass_check_integer" will be created and it will be assigned True
pass_check_float = isinstance(a_float, float)  #prediction: a variable called "pass_check_float" will be created and it will be assigned True
pass_check_boolean_as_bool = isinstance(a_boolean, bool) #prediction: a variable called "pass_check_boolean" will be created and it will be assigned True
pass_check_boolean_as_int = isinstance(a_boolean, int) # Booleans can be integers: True = 1, False = 0  #prediction: a variable called "pass_check_boolean_as_int" will be created and it will be assigned True

# failing
fail_check_string = isinstance(a_string, bool) #prediction: a variable called "fail_check_string" will be created and it will be assigned False
fail_check_integer = isinstance(an_integer, float) #prediction: a variable called "fail_check_integer" will be created and it will be assigned False
fail_check_float = isinstance(a_float, int)  #prediction: a variable called "fail_check_float" will be created and it will be assigned False
fail_check_boolean = isinstance(a_boolean, str) #prediction: a variable called "fail_check_boolean" will be created and it will be assigned False

print("end of script")
