#Desinged by VVL

import math
import sys

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False 

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3,sqr,2):
        if n % divisor == 0:
            return False
    return True

def is_coprime(a,b):
    if math.gcd(a,b) == 1:
        return True
    else:
        return False

# Sys import for console example
# >> python Key_gen.py -pq 2 3 -e 1
# >> sys.argv -> [Key_gen.py, -pq, 2, 3, -x, 1]

if '-pq' in sys.argv:
    flag_index = sys.argv.index('-pq')
    flag_index += 1
    p = int(sys.argv[flag_index])
    flag_index += 1
    q = int(sys.argv[flag_index])
else:# If you don't provide a couple of prime numbers, they will be 89 and 97
    p = 89
    q = 97
    
if not is_prime(p) or not is_prime(q):
    raise ValueError('P and Q must be prime')

if '-e' in sys.argv:
    flag_index = sys.argv.index('-e')
    flag_index += 1
    e = int(sys.argv[flag_index])
else:
    e = 1


n = int(p * q)

# z = Euler Function
z = int((p-1) * (q-1))

# If the 'e' you provide is not a 'z' coprime, the program will find the next coprime of z larger than 'e'
while math.gcd(e,z) != 1 :
    e += 1

for d in range(2,z):
    if (d*e)%z == 1:
        break


print(f"Public key: {e}")
print(f"Private Key: {d}")
print(f"n = p * q = {n}")
