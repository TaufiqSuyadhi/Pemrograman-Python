# contoh9_2 - Halaman 324
# Buku Pemrograman Python RH Sianipar
# Deskripsi: Membuat oyek dari suatu kelas
# -------------------------------------------

class Mahasiswa:
    nama = "Taufiq DS Suyadhi"
    nim = "1234567"
    ipk = 3.67

    def tampil(self):
        print("Nama:",self.nama)
        print("NIM:" ,self.nim)
        print("IPK:" ,self.ipk)

# Membuat obyek
Teknik_Elektro = Mahasiswa()
Teknik_Elektro.tampil()