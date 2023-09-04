"""
array -> TIPE DATA yang bisa menyimpan banyak nilai
"""

yourName = ["Mitsuha", "Taki", "Yotsuha", "Okudera", "Tesi"]
# array mempunyai index, yaitu urutan sebuah nilai dalam array
# index dimulai dari 0

heroine = yourName[0] 
print(heroine) # > Mitsuha

print(yourName[1]) # > Taki
print(yourName[3]) # > Okudera

# MENAMBAHKAN NILAI PADA ARRAY bisa menggunakan fungsi "append"
x = [10, 20, 30, 40]
x.append(50) 
print(x) # > 10, 20, 30, 40, 50

# MENGELUARKAN NILAI PADA ARRAY bisa menggunakan fungsi "pop"
x.pop() # mengeluarkan nilai terakhir
print(x) # > 10, 20, 30, 40

y = [1, 2, 3, 4]
y.pop(1) # mengeluarkan index no 1
print(y) # > 1, 3, 4

# MENGHITUNG PANJANG ARRAY bisa menggunakan fungsi "len()"
jjk = ["Yuuji", "Megumi", "Nobara", "Gojo", "Yuta", "Maki", "Inumaki"]
length_of_member = len(jjk)
print(length_of_member) # > 7

# MENGURUTKAN ARRAY bisa dengan ascending dan descending
jjk.sort() # Ascending (atas ke bawah) // bisa juga jjk.sort(reverse=False)
print(jjk)

jjk.sort(reverse=True) 
print(jjk) # Descending (bawah ke atas)