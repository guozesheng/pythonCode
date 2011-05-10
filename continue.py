#!/usr/bin/python
# Filename : continue.py

while True:
    s = raw_input("Enter someting:")
    if s == "quit":
        break;
    if len(s) < 3:
        continue
    print "Input is of sufficient length" 

