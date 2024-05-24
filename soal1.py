# Input data mahasiswa dan nilai mereka
mahasiswa = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# Mengambil nilai unik dan mengurutkannya secara ascending
nilai_unik = sorted(set(nilai for nama, nilai in mahasiswa))

# Mengambil nilai terendah kedua
nilai_terendah_kedua = nilai_unik[1]

# menyimpan nama mahasiswa dengan nilai terendah kedua
siswa_terendah_kedua = []

# Memeriksa mahasiswa untuk mencari nilai terendah kedua
for nama, nilai in mahasiswa:
    if nilai == nilai_terendah_kedua:
        siswa_terendah_kedua.append(nama)

# Mengurutkan nama mahasiswa secara alphabet
siswa_terendah_kedua.sort()

# Mencetak nama mahasiswa pada baris baru
for nama in siswa_terendah_kedua:
    print(nama)
