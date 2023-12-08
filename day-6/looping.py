# LOOPING DI PYTHON ADA 3 :

# for loop -> jika sudah diketahui mau ngulang berapa banyak
for i in range(10):
    print(i)

# output : 0 1 2 3 4 5 6 7 8 9
# kenapa cuman sampai 8? ya krn loop mulainya dr angka 0, coba hitung itu ada brp angka

for x in range(1, 10):
    print(x)

# output : 1 2 3 4 5 6 7 8 9 
# kenapa cuman 1 - 9 aja yg keprint? iya, 10 gak dihitung, kalo mau print 10 juga, ubah range jadi (1, 11)
print("\n")

total = 0
for n in range(1, 11):
    print(f"Hello World, aku perulangan ke-{n}")
    total += n

print(f"Total dari semuanya adalah: {total}\n")

for y in range(1, 10):
    print(y)
    if y == 5:
        break # kalau sampai 5 bakal berenti
print("\n")

# -------------------------------------------------------
# while loop : ngeceknya pakai statement boolean
n = 0
while n <= 5:
    print(n)
    n += 1
print("Loop selesai")
# output : 1 2 3 4 5
# kalau tidak ada increment, ya nilai n nya 0 terus, bakal jadi infinite loop

print("\n")
# contoh kombinasi while true dengan kondisi
from time import sleep
x = 0

while True:
    print(f"Berulang dan berulang - ini ke-{x}")
    
    if x == 10:
        break # Untuk menghentikan perulangan

    x = x + 1
    sleep(1)

print("Perulangan selesai\n")
# -------------------------------------------------------
# for each loop : looping thd nilai array
data = [1, 4, 5, 1]

for x in data:
    print(x)

# CONTOH KOMBINASI ARRAY, DICTIONARY, KONDISI DAN LOOP
data = []

while True:
    name = input("Masukkan nama anda: ")
    age = input("Masukkan umur anda: ")
    age = int(age) # Kita ubah tipe data age dari string menjadi integer, karena default input adalah string
    
    item = {"name": name, "age": age}
    data.append(item)
    
    print("Berhasil menambahkan data baru!")
    opsi = input("Apakah anda ingin menambahkan data lagi (y/n): ")
    opsi = opsi.lower() # Kita kecilkan hurufnya agar apabila diinput Y tetap dihitung sebagai y
 
    if opsi == "y":
        print("Silahkan kembali menambahkan data \n")
    else:
        print("Program dihentikan")
        break

print("\nProgram berhenti.")
print("Data yang berhasil terkumpul adalah: \n")

for item in data:
    print(f"Nama: {item['name']} - Usia: {item['age']}")