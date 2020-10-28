import gmpy2

# Note: you do not need gmpy2 if you use small numbers, you
# could have also use the built-in pow() function. Check
# the official documentation for more information on pow()

number_to_encrypt = 512

##############################################################
# SETUP

# We choose two big primes, here we use small primes
# for the sake of simplicity
p = 67
q = 83
e = 59

# Small note: if the number to encrypt has more digits than
# the modulus the algorithm won't work

# We find n
n = p*q

# and phi(n) which should be coprime with phi(n)
phi_n = (p-1)*(q-1)

e = 59

# This function returns True if coprime_to_check is coprime with phi_n


def is_coprime_phi(phi_n, coprime_to_check):
    while phi_n % coprime_to_check == 0:
        coprime_to_check = input(
            "Enter a prime number, to check if coprime with phi_n")
        e = coprime_to_check
    return True


# If e is not coprime with phi(n) ValueError is raised
if not is_coprime_phi(phi_n, e):
    raise ValueError("e is not coprime with phi_n")

# The following code finds the modular multiplicative inverse


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(coprime, phi_n):
    g, x, y = egcd(coprime, phi_n)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi_n


# The modular multiplicative inverse
d = modinv(e, phi_n)

# Public key
pub_k = [e, n]

# Private key
priv_k = [d, n]

# Encrypting and decrypting functions


def encrypt_this(m):
    result = gmpy2.powmod(m, e, n)
    return result


def decrypt_this(c):
    plain = gmpy2.powmod(c, d, n)
    return plain

###########################################################


# Encrypt
enc = encrypt_this(number_to_encrypt)
print("Encrypted number: ", enc)

# Decrypt
dec = decrypt_this(enc)
print("Decrypted plain number: ", dec)
