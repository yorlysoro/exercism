"""
Diffie-Hellman Algorithm
"""
import random


def public_key(prime, g, private):
    return int((g ** private) % prime)


def private_key(prime):
    while True:
        n = random.randint(0, prime)
        if n > 1 and n < prime:
            break
    return n


def secret(prime, public_key_share, private_key_share):
    s = public_key(prime, public_key_share, private_key_share)
    return s


p = 23
g = 5
alice_private_key = private_key(p)
bob_private_key = private_key(p)
alice_public_key = public_key(p, g, alice_private_key)
bob_public_key = public_key(p, g, bob_private_key)
secret_a = secret(p, bob_public_key, alice_private_key)
secret_b = secret(p, alice_public_key, bob_private_key)
print(secret_a == secret_b)
