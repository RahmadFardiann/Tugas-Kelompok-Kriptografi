def generate_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        if plaintext[i].islower():  # Enkripsi huruf kecil
            x = (ord(plaintext[i]) - ord('a') + ord(key[i].lower()) - ord('a')) % 26
            ciphertext.append(chr(x + ord('a')))
    return "".join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    for i in range(len(ciphertext)):
        if ciphertext[i].islower():  # Dekripsi huruf kecil
            x = (ord(ciphertext[i]) - ord('a') - (ord(key[i].lower()) - ord('a')) + 26) % 26
            decrypted_text.append(chr(x + ord('a')))
    return "".join(decrypted_text)

# Input plaintext dan key
plaintext = "dilarangmeroko"
key = "kunci"

# Sesuaikan panjang key dengan plaintext
key = generate_key(plaintext, key)

# Enkripsi menggunakan Vigenère cipher
ciphertext = vigenere_encrypt(plaintext, key)

# Dekripsi menggunakan Vigenère cipher
decrypted_text = vigenere_decrypt(ciphertext, key)

# Tampilkan hasil
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
