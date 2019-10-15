#!/usr/bin/env python3
from textwrap import wrap

def hash(plainString):
    hashed = plainString
    # do hashing stuff here
    return hashed

def main():
    """ Main entry point of the app """
    print("hello world")
    inputStr = input("Enter string to be hashed: ")
    n = len(inputStr)//4
    a = inputStr[0:n]
    b = inputStr[n:n*2]
    c = inputStr[n*2:n*3]
    d = inputStr[n*3:len(inputStr)]
    print(a)
    print(b)
    print(c)
    print(d)
    if len(a) == 0 or len(b) == 0 or len(c) == 0 or len(d) == 0:
        raise Exception('Error string not long enough')
    print(f'Hashed string: {hash(inputStr)}')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()