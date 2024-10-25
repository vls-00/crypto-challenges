from pwn import xor

print(f'Flag: Crypto{{{xor("label", 13)}}}')