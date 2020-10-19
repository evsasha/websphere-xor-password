#!/usr/bin/env python3

#
# Python script to decode|encode websphere {XOR} password.
#

import argparse
import base64

# Read arguments
parser = argparse.ArgumentParser(description='Decode|encode WebSphere passwords that use {xor} prepended tag.')
parser.add_argument('password', help='Password to decode|encode')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--decode', dest='decode', action='store_true', help='Decode password')
group.add_argument('-e', '--encode', dest='encode', action='store_true', help='Encode password')
args = parser.parse_args()

def strXor (string):
    """ String XOR, base '_' """
    l = [ chr ( ord(c) ^ ord ('_') ) for c in string ]
    return ''.join(l)

def decodePassword (password):
    """ Decode encrypted password """
    # Remove '{XOR}' prefix
    if password.lower().startswith("{xor}"):
        password = password[5:]
    return strXor(base64.b64decode(password).decode())
    
def encodePassword (password):
    """ Encode password """
    pXor = strXor(password)
    pBase64 = base64.b64encode(str.encode(pXor)).decode()
    return "{XOR}" + pBase64

def main():
    if args.decode:
        print("> Decode mode")
        print("> Decoded password: " + decodePassword(args.password))
    elif args.encode:
        print("> Encode mode")
        print("> Encoded password: " + encodePassword(args.password))

if __name__ == "__main__":
    main()
