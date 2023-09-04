# penggunaan f-string ditujukan untuk ngeprint beda variabel
x = 10
print(f"Nilai x adalah {x}\n") #contoh penggunaan f-string
# \n adalah newline

# input CLI (command line interface)
nama = input("Silakan ketik nama Anda: ")
print(f"Nama Anda adalah: {nama}")

# operator assignment -> memberikan nilai baru
x = 10
# x = x + 10

"""
Baris di atas bisa disingkat menjadi
x += 10
"""
x += 10
print(x)