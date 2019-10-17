#!/usr/bin/env python3
import binascii

# from https://stackoverflow.com/a/7397689
def text_to_bits(text, encoding="utf-8", errors="surrogatepass"):
    """ Takes text and return a string of binary """
    bits = bin(int.from_bytes(text.encode(encoding, errors), "big"))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding="utf-8", errors="surrogatepass"):
    """ Takes string of binary and return a string """
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode(encoding, errors) or "\0"


def strToNum(string):
    """ translate a string to a string of numbers """
    if len(string) <= 0:
        return ""
    temp = ""
    for char in string:
        temp += str(ord(char))
    return temp

def numToBin(string):
    """ Take a number and return a string of binary """
    return text_to_bits(str(int(bitShift(string)) % 1234))

def bitShift(ary):
    shiftVal = 3
    intAry = []
    rtnString = ""

    for x in ary:
        intAry.append(ord(x))

    for y in intAry:
        newString = str(y << shiftVal)
        rtnString += newString

    return rtnString

def functionF(a,c,d):
    """ Should return a number """
    return strToNum(a)

def functionG(a,c,d):
    """ Should return a number """
    return strToNum(a)

def hash(plainString):
    """ Take a string and return hashed value """
    # hashed = plainString
    n = len(plainString) // 4

    a = plainString[0:n]
    b = plainString[n : n * 2]
    c = plainString[n * 2 : n * 3]
    d = plainString[n * 3 : len(plainString)]

    if len(a) == 0 or len(b) == 0 or len(c) == 0 or len(d) == 0:
        raise Exception("Error string not long enough, use at least 4 characters")

    numA = numToBin(functionF(a,c,d))
    numB = numToBin(strToNum(b))
    shiftC = numToBin(c)
    numD = numToBin(functionG(a,c,d))

    # hashed = A + B + shiftC + D
    hashed = numA + '|' + numB + '|' + shiftC + '|' + numD
    return hashed


def main():
    """ Main entry point of the app """
    inputStr = input("Enter string to be hashed: ")
    print(f"Hashed string: {hash(inputStr)}")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
