#!/usr/bin/env python3
import binascii

def hash(plainString):
    hashed = plainString
    # do hashing stuff here
    return hashed

# from https://stackoverflow.com/a/7397689
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def binaryToLetters(binA,binB,binC,binD):
    a = binascii.b2a_uu(binA)
    print(a)
    return {'a':a,'b':b,'b':b,'b':b}

def lettersToResult(a,b,c,d):
    result = a + b + c + d
    return result

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

    print(text_from_bits(text_to_bits('hello')) == 'hello')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()