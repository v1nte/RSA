#Desinged by VVL

import sys

def extract_info(flag):
    i = sys.argv.index(flag) + 1 
    return sys.argv[i]

# -n is pq product
if '-n' not in sys.argv:
    print("Your must provide n using the -pq flag")
    sys.exit(1)

# --key is the decrypting key
if '--key' not in sys.argv:
    print("Your must provide yout key using the --key flag")
    sys.exit(1)

# -M is the encrypted message you want to decryp
if '-M' not in sys.argv:
    print("Your must provide a encrypted message using the -M flag")
    sys.exit(1)

# How to run example
# >> python Decrypting.py -n 123 --key 123 -M 123

n = int(extract_info('-n'))
d = int(extract_info('--key'))
M = int(extract_info('-M'))

# Finally you get the original message
m = (M**d) % n

print(f"your dencrypted message is {m}")
