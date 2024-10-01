import numpy as np

# Membuat matriks 5x5 berdasarkan kunci
def create_matrix(key):
    alphabet = "abcdefghiklmnopqrstuvwxyz"  # Menghilangkan huruf 'j'
    matrix = []
    used_letters = []

    for char in key:
        if char not in used_letters and char in alphabet:
            matrix.append(char)
            used_letters.append(char)

    for char in alphabet:
        if char not in used_letters:
            matrix.append(char)

    return np.array(matrix).reshape(5, 5)

# Membagi plaintext menjadi pasangan huruf
def prepare_text(text):
    text = text.replace('j', 'i')  # Gantikan 'j' dengan 'i'
    prepared_text = ""
    i = 0

    while i < len(text):
        if i == len(text) - 1:
            prepared_text += text[i] + 'x'
            i += 1
        elif text[i] == text[i + 1]:
            prepared_text += text[i] + 'x'
            i += 1
        else:
            prepared_text += text[i] + text[i + 1]
            i += 2

    return prepared_text

# Mendapatkan posisi karakter dalam matriks
def get_position(char, matrix):
    result = np.where(matrix == char)
    return result[0][0], result[1][0]

# Enkripsi Playfair
def playfair_encrypt(plaintext, matrix):
    ciphertext = ""
    prepared_text = prepare_text(plaintext)

    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i + 1]
        row1, col1 = get_position(char1, matrix)
        row2, col2 = get_position(char2, matrix)

        if row1 == row2:  # Sama baris
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Sama kolom
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Bentuk persegi panjang
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

# Dekripsi Playfair
def playfair_decrypt(ciphertext, matrix):
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = get_position(char1, matrix)
        row2, col2 = get_position(char2, matrix)

        if row1 == row2:  # Sama baris
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Sama kolom
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Bentuk persegi panjang
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext

# Input plaintext dan key
plaintext = "infongopi"
key = "kopi"

# Buat matriks dari kunci
matrix = create_matrix(key)

# Enkripsi menggunakan Playfair cipher
ciphertext = playfair_encrypt(plaintext, matrix)

# Dekripsi menggunakan Playfair cipher
decrypted_text = playfair_decrypt(ciphertext, matrix)

# Tampilkan hasil
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print("Matrix:\n", matrix)
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
