def mod_exp(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def diffie_hellman(p, g):
    alice_private = 6
    bob_private = 15

    alice_public = mod_exp(g, alice_private, p)
    bob_public = mod_exp(g, bob_private, p)

    alice_secret = mod_exp(bob_public, alice_private, p)
    bob_secret = mod_exp(alice_public, bob_private, p)

    print("Shared secret computed by Alice:", alice_secret)
    print("Shared secret computed by Bob:", bob_secret)

parameter1 = 23
parameter2 = 5
diffie_hellman(parameter1, parameter2)
