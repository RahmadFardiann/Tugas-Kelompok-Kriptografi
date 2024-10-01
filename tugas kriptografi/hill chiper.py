import numpy as np

# Fungsi untuk mengonversi karakter ke angka
def char_to_num(c):
    return ord(c) - 97

# Fungsi untuk mengonversi angka ke karakter
def num_to_char(n):
    return chr(n + 97)

# Fungsi enkripsi menggunakan Hill Cipher
def encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "")  # Menghilangkan spasi
    if len(plaintext) % 3 != 0:  # Hill Cipher biasanya menggunakan matriks 3x3
        plaintext += 'x' * (3 - len(plaintext) % 3)  # Tambahkan padding 'x' jika perlu
    
    ciphertext = ''
    for i in range(0, len(plaintext), 3):
        # Ambil 3 karakter dari plaintext dan ubah ke bentuk vektor
        vec = np.array([char_to_num(c) for c in plaintext[i:i+3]])
        # Kalikan dengan key_matrix dan mod 26
        enc_vec = np.dot(key_matrix, vec) % 26
        # Ubah hasil enkripsi kembali menjadi karakter
        ciphertext += ''.join([num_to_char(int(num)) for num in enc_vec])
    
    return ciphertext

# Kunci matriks 3x3 (mod 26)
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

# Plaintext yang akan dienkripsi
plaintext = "ayo semangat"

# Enkripsi
ciphertext = encrypt(plaintext, key_matrix)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
