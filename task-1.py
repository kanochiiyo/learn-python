"""
Terdapat nilai x dan y, bagaimana cara menukar nilai 
tersebut tanpa menggantinya secara langsung?

Bagaimana cara menukar nilai agar x menjadi 10 dan y menjadi 20?

Clue: Gunakan satu variabel temporary
"""

x = 20
y = 10

temp = x
x = y
y = temp

# print("X =", x)
# print("Y =", y)
# print("X = " + str(x)) # str(x) -> ubah tipe data int ke string

# lebih baik gunakan f-string
print(f"X = {x}")
print(f" = {y}")