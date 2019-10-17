#!/usr/bin/env python3
import binascii

# from https://stackoverflow.com/a/7397689
def text_to_bits(text, encoding="utf-8", errors="surrogatepass"):
    bits = bin(int.from_bytes(text.encode(encoding, errors), "big"))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding="utf-8", errors="surrogatepass"):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode(encoding, errors) or "\0"


def binaryFinalResult(a, b, c, d):
    result = a + b + c + d
    return text_from_bits(result)


def strToNum(string):
    if len(string) <= 0:
        return ""
    temp = ""
    for char in string:
        temp += str(ord(char))
    return temp

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
    inputStr = input("Enter string to be hashed: ")
    n = len(inputStr) // 4
    a = inputStr[0:n]
    numA = strToNum(a)
    b = inputStr[n : n * 2]
    numB = strToNum(b)
    c = inputStr[n * 2 : n * 3]
    numC = strToNum(c)
    d = inputStr[n * 3 : len(inputStr)]
    numD = strToNum(d)
    print(numA)
    print(numB)
    print(numC)
    print(numD)

    print(format(12, "b"))
    print(format(25, "b"))

    print(format(int("1100", 2) + int("11001", 2), "b"))
    print(format(int(format(12, "b"), 2) + int(format(25, "b"), 2), "b"))

    print(int(format(int(format(12, "b"), 2) + int(format(25, "b"), 2), "b"), 2))

    if len(a) == 0 or len(b) == 0 or len(c) == 0 or len(d) == 0:
        raise Exception("Error string not long enough, use at least 4 characters")
    print(f"Hashed string: {hash(a,b,c,d)}")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
