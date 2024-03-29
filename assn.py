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
    return text_to_bits(str(int(bitShift(string)) % 1000))

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

def functionF(a,d):
    """ Should return a string of a number """
    intA = []
    intD = []
    rtnString = ''

    for x in a:
        intA.append(ord(x))
    for y in d:
        intD.append(ord(y))
    l = min(len(intA), len(intD))
    for num in range(l):
        newString = str(intA[num] ^ intD[num])
        rtnString += newString

    return rtnString

def functionG(a,b,c,d):
    """ Should return a string of a number """
    intArr = []
    comboArr = a + b + c + d
    for x in comboArr:
        intArr.append(ord(x))

    return str(sum(intArr))

def numbersToLetters(number):
    """
    Take a string of number and convert into characters
    """
    arr = [number[i:i+2] for i in range(0, len(number), 2)]
    result = ''
    for i in arr:
        i = int(i)
        if(i<=48):
            i = i + 48
        result += chr(i)
    return result

def hash(plainString):
    """
    Main hashing function for hashing 
    Run the hashhelper function 12 times
    """
    result = plainString
    for i in range(0,12):
        result = hashHelp(result)
    return result

def hashHelp(plainString):
    """ Take a string and return hashed value """
    # hashed = plainString
    n = len(plainString) // 4

    a = plainString[0:n]
    b = plainString[n : n * 2]
    c = plainString[n * 2 : n * 3]
    d = plainString[n * 3 : len(plainString)]

    if len(a) == 0 or len(b) == 0 or len(c) == 0 or len(d) == 0:
        raise Exception("Error string not long enough, use at least 4 characters")

    numA = numToBin(functionF(a,d))
    numB = numToBin(strToNum(b))
    numC = numToBin(bitShift(c))
    numD = numToBin(functionG(a,b,c,d))

    # hashed = A + B + numC + D
    # hashed = numA + '|' + numB + '|' + numC + '|' + numD
    hashed = text_from_bits(numD + numA + numB + numC)
    hashed = numbersToLetters(hashed)
    return hashed


def main():
    """ Main entry point of the app """
    inputStr = input("Enter string to be hashed: ")
    print(f"Hashed string: {hash(inputStr.replace(' ', ''))}")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
