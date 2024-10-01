# Caesar cipher shift value
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - shift_base - shift + 26) % 26 + shift_base)
        else:
            decrypted += char
    return decrypted

# Vigenère cipher encryption
def vigenere_encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            x = (ord(plaintext[i]) - ord('A') + ord(key[i % len(key)]) - ord('A')) % 26
            ciphertext.append(chr(x + ord('A')))
    return "".join(ciphertext)

# Vigenère cipher decryption
def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            x = (ord(ciphertext[i]) - ord('A') - (ord(key[i % len(key)]) - ord('A')) + 26) % 26
            decrypted_text.append(chr(x + ord('A')))
    return "".join(decrypted_text)

# Super Encryption using Caesar cipher and Vigenère cipher
def super_encrypt(plaintext, vigenere_key, caesar_shift):
    # Step 1: Vigenère encryption
    vigenere_encrypted = vigenere_encrypt(plaintext, vigenere_key)
    
    # Step 2: Caesar encryption
    caesar_encrypted = caesar_encrypt(vigenere_encrypted, caesar_shift)
    
    return caesar_encrypted

# Super Decryption using Caesar cipher and Vigenère cipher
def super_decrypt(ciphertext, vigenere_key, caesar_shift):
    # Step 1: Caesar decryption
    caesar_decrypted = caesar_decrypt(ciphertext, caesar_shift)
    
    # Step 2: Vigenère decryption
    vigenere_decrypted = vigenere_decrypt(caesar_decrypted, vigenere_key)
    
    return vigenere_decrypted

# Input plaintext, Vigenère key, and Caesar shift
plaintext = "TUTORDEKK"
vigenere_key = "KEY"
caesar_shift = 3

# Enkripsi
ciphertext = super_encrypt(plaintext, vigenere_key, caesar_shift)

# Dekripsi
decrypted_text = super_decrypt(ciphertext, vigenere_key, caesar_shift)

# Tampilkan hasil
print(f"Plaintext: {plaintext}")
print(f"Vigenère Key: {vigenere_key}")
print(f"Caesar Shift: {caesar_shift}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
