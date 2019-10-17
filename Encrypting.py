#Desinged by VVL

import sys

def extract_info(flag):
    i = sys.argv.index(flag) + 1 
    return sys.argv[i]

# -n is pq product
if '-n' not in sys.argv:
    print("Your must provide n using the -n flag")
    sys.exit(1)

# --key is the encrypting key
if '--key' not in sys.argv:
    print("Your must provide your key using the --key flag")
    sys.exit(1)

# -m is the message you want to encrypt
if '-m' not in sys.argv:
    print("Your must provide a message using the -m flag")
    sys.exit(1)
# 'M' will be the encrypted message

# How to run example
# >> python Ecnrypting.py -n 123 --key 123 -m 123

n = int(extract_info('-n'))
e = int(extract_info('--key'))
m = int(extract_info('-m'))

M = (m**e) % n

print(f"your encrypted message is {M}")
