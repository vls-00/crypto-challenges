from pwn import xor

encoded = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

prefix = r"crypto{"

# Keep only the prefix characters from the encoded text
prefix_encoded = bytes.fromhex(encoded[:14])

first_7_chr_of_key = xor(prefix_encoded, prefix.encode())
print(f'The 7 first characters of the key: "{first_7_chr_of_key.decode('ascii')}"')

flag = xor(bytes.fromhex(encoded), "myXORkey".encode()).decode('ascii')
print(flag)