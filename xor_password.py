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

def removePrefix (string):
    """ Remove '{XOR}' prefix """
    if string.lower().startswith("{xor}"):
        return string[5:]
    else:
        return string

def btxor (bytes):
    """ Bytewise XOR, base '_' """
    l = [ chr ( b ^ ord ('_') ) for b in bytes ]
    return ''.join(l)

def decodePassword (encodedPassword):
    """ Decode encrypted password """
    p = removePrefix(encodedPassword)
    pDecodedB64 = base64.b64decode(p)
    pDecoded = btxor(pDecodedB64)
    return pDecoded
    
def encodePassword (password):
    """ Encode password """
    p = removePrefix(password)
    pBytes = str.encode(p)
    pEncodedXor = btxor(pBytes)
    pEncodedB64 = base64.b64encode(str.encode(pEncodedXor))
    pEncoded = "{XOR}" + pEncodedB64.decode()
    return pEncoded

def main():
    if args.decode:
        print("> Decode mode")
        print("> Decoded password: " + decodePassword(args.password))
    elif args.encode:
        print("> Encode mode")
        print("> Encoded password: " + encodePassword(args.password))

if __name__ == "__main__":
    main()
