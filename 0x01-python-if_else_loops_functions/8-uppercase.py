#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        i = ord(i)
        if 97 <= i <= 122:
            i = i - 32
        res += chr(i)
    print(res)
