# Impor modul math biar bisa pakai fungsi sqrt (akar)
import math

print("Program Menghitung Hipotenusa Segitiga Siku-siku\n")

# User input nilai a dan b
a = float(input("Masukkan panjang sisi pertama (a) = "))
b = float(input("Masukkan panjang sisi kedua (b) = "))

# Gunakan pythagoras untuk nyari nilai hipotenusa (sisi miring)
c = math.sqrt(a**2 + b**2) # ** adalah operator perpangkatan

# Tampilkan nilai panjang hipotenusa
print(f"Panjang hipotenusa = {c}") # Gunakan f-string
