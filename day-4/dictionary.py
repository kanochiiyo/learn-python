"""
dictionary -> object yang bisa ditampilkan jika kita memanggil keynya
"""

# dictionary sama seperti array, bedanya dictionary memiliki key yang bisa disummon

data = {
    "name": "Dinn",
    "occupation": "College student",
    "company": "UPN Veteran Yogyakarta",
    "hobbies": ["watching anime", "reading manga", "sleep"],
    "birth_year": "2004"
}

print(data['name'])

# MENCETAK SALAH SATU NILAI DI ARRAY
hobi = data['hobbies'][0] # masukkan index
print(hobi, "\n")

# MENGOLAH DICTIONARY
data['name'] = "Andini" # menimpa nilai
data['age'] = 19 # menambahkan key baru

print(data, "\n")

del data['company']
print(data)