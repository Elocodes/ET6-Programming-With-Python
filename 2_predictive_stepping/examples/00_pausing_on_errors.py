#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Pausing on Errors

By default, the debugger will stop on errors and show what went wrong.
    
You can change this setting in the breakpoints pane down left.
        
"""

a = 1   # I predict that a variable a will be created and the value 1 assigned to it

b = "2"  # I predict that a variable b will be created and the str "2" assigned to it

# the error message will appear below this line
#   and the values in memory can help you understand what went wrong
c = a + b   # I predict that this will throw up an error because you cannot add int and str

print(c)
