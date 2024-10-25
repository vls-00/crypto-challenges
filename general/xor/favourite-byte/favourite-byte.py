from pwn import xor

encoded = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encoded_bytes = bytes.fromhex(encoded)

for i in range(256):
    decoded = xor(encoded_bytes, i.to_bytes(1))
    
    # We use a try catch because some values might not be able to get decoded to ASCII characters and raise an exception
    try:
        if("crypto{" in decoded.decode('ascii')):
            print(f"Key: {i}")
            print(f"Flag: {decoded.decode('ascii')}")
            exit(0)
    except Exception:
        continue

print("Flag was not found")