# Tuple

# Note: Uncomment blok program yang akan di run

'''
# Membuat tuple
data_tuple = ("jahe","kunyit","kencur", 5, 4, 9)
print(data_tuple)
print(data_tuple[:2])   # Menampilkan 2 elemen pertama
print(data_tuple[-1])   # Menampilkan elemen terakhir
'''

'''
# Mencoba mengubah elemen tuple     --> error
data1_tuple = ("Jawa","Bali","NTT","NTB")
print(data1_tuple)
data1_tuple[2] = "Kepri"    # Upaya mengubah elemen tuple
'''

'''
# Tuple dengan Elemen Tunggal
A = ("Robonesia")
print("Tipe data A adalah = ", type(A) )     # Cek tipe data variable A
B = (27)
print("Tipe data B adalah = ", type(B) )     # Cek tipe data variable B

C = ("Robonesia",)
print("Tipe data C adalah = ", type(C) )    # Cek tipe data variable C
D = (27,)
print("Tipe data D adalah = ", type(D) )     # Cek tipe data variable D
'''

'''
# 1. Operasi Aritmatika Pada Tuple
herbal = ('Jahe', 'Temulawak', 'Kencur')
print(herbal)
herbal=herbal + ('Kunyit', 'Ginseng', 1, 2, 3)    # Penjumlahan
print(herbal)

angka = (25, 27)
angka = angka * 3         # Perkalian
print(angka)
'''

'''
# 2. Operasi Keanggotaan Pada Tuple
data1_tuple = (11, 17, 19, 27, 37, 47)
print("Apakah 11 anggota tuple? ==> ",11 in data1_tuple)
print("Apakah 15 anggota tuple? ==> ",15 in data1_tuple)
print("Apakah 27 anggota tuple? ==> ",27 in data1_tuple)
'''

'''
# 3. Operasi Min-Max Pada Tuple
data1_tuple = (27, 17, 19, 47, 37, 11)
print("Nilai minimum tuple = ",min(data1_tuple))
print("Nilai maximum tuple = ",max(data1_tuple))
'''

'''
# 4. Operasi Menghapus Tuple
data1_tuple = (11, 17, 19)
data2_tuple = ("Wonogiri","Solo","Jogja")
del data2_tuple         # Menghapus data2_tuple
print("Data tuple 1 = ", data1_tuple)
print("Data tuple 2 = ", data2_tuple)
'''

'''
# 5. Operasi Mengemas Tuple
(empat,lima,enam) = (4,5,6)         # Cara 1 - Mengemas tupple
tujuh,delapan, sembilan = 7,8,9     # Cara 2 - Mengemas tupple
print(empat,lima,enam)
print(tujuh,delapan,sembilan)
'''

'''
# 6. Operasi Menukar Data Tuple
U = 30
V = 70
U,V = V,U    # Proses mengemas tuple & penukaran datanya

print('Nilai data U = ', U)     # Nilai variabel U
print('Nilai data V = ', V)     # Nilai variabel V
'''

'''
# Konversi Tuple Menjadi List
data_tuple2 = ('Taufiq',377,477)     # Data tuple
T = list(data_tuple2)                # Konversi tuple menjadi list
print("Hasil konversi tuple menjadi list = ", T)
print("Tipe data variabel T adalah = ", type(T))     # Tipe tuple sudah berubah menjadi list
'''



