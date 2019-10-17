#!/usr/bin/env python3
from textwrap import wrap

def bitShift(ary):
    shiftVal = 3
    intAry = []
    rtnString = ''

    for x in ary:
        intAry.append(ord(x))

    for y in intAry:
        newString = str(y << shiftVal)
        rtnString += newString

    return rtnString

def hash(plainString):
    # hashed = plainString
    n = len(plainString)//4
    c = plainString[n*2:n*3]
    shiftC = bitShift(c)
    # hashed = A + B + shiftC + D
    hashed = shiftC
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
