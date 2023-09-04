# KONDISI IF ELSE DAN ELIF 

x = 100
y = 100

# IF ELSE -> else merupakan kondisi default yg dijalankan jika if bernilai false
# kode berjalan dari atas ke bawah, 
# jika perintah sebelumnya bernilai true,
# maka perintah di bawahnya tidak dijalankan
if y > x: # false
    print("y lebih besar dari x") 
elif y == x: # true
    print("y sama dengan x")
else: # false
    print("y lebih kecil dari x")
# > y sama dengan x

# KONDISI PADA ARRAY
z = [1, 2, 3, 4, 5]

lima = 5

if lima in z:
    print("5 ada di dalam array z")
else:
    print("5 tidak ada di dalam array")

# KONDISI DENGAN OPERATOR
job = "Student"
age = 25
location = "Malang"

isEligible = job == "Student" and age > 21  # Boolean
isLivedInJakarta = location == "Jakarta"

if isEligible and isLivedInJakarta:
    print("Kamu boleh masuk")
else:
    print("Kamu tidak boleh masuk")