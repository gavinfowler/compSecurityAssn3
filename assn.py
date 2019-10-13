#!/usr/bin/env python3

def hash(plainString):
    hashed = plainString
    # do hashing stuff here
    return hashed

def main():
    """ Main entry point of the app """
    print("hello world")
    inputStr = input("Enter string to be hashed: ")
    print(f'Hashed string: {hash(inputStr)}')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()