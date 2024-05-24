if __name__ == '__main__':
    N = int(input())  # Membaca jumlah perintah
    daftar = []  # Inisialisasi daftar kosong

    # Membaca dan menjalankan setiap perintah
    for _ in range(N):
        perintah = input().split()  # Membaca perintah dari input dan memisahkan kata-katanya

        # Memproses perintah
        if perintah[0] == 'insert':
            daftar.insert(int(perintah[1]), int(perintah[2]))
        elif perintah[0] == 'print':
            print(daftar)
        elif perintah[0] == 'remove':
            daftar.remove(int(perintah[1]))
        elif perintah[0] == 'append':
            daftar.append(int(perintah[1]))
        elif perintah[0] == 'sort':
            daftar.sort()
        elif perintah[0] == 'pop':
            daftar.pop()
        elif perintah[0] == 'reverse':
            daftar.reverse()
