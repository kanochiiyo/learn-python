
"""
Sebagai software engineer, kamu ditantang untuk membuat program simulasi sebuah keranjang belanja online.
Program tersebut dapat membuat tiga fitur:

1. Melihat isi keranjang
2. Menambahkan isi keranjang
3. Menghitung total isi keranjang
4. Keluar

Clue:
Untuk membuat keranjang, gunakan list (array) dan dictionary (object), samplenya adalah variabel product.

"""

products = [
    {"name": "Laptop", "price": 800, "quantity": 10},
    {"name": "Smartphone", "price": 500, "quantity": 20},
    {"name": "Headphones", "price": 100, "quantity": 30},
]

"""
Algoritma

1. Buatlah variable carts dengan tipe array dan buatlah While (Endless Loop)
2. Terima input pilihan menu dari pengguna
3. Buat tiga kondisi
4. Apabila pilihan melihat ditekan, maka yang harus dilakukan melakukan looping terhadap variable carts. Cetak dengan format sebagai berikut: Barang - {nama} | Harga: {price} | Jumlah yang dibeli: {qty}
5. Apabila pilihan isi keranjang ditekan, maka yang harus dilakukan adalah menerima dua input baru yaitu nama barang dan quantity
6. Apabila pilihan menghitung total isi keranjang ditekan, maka melakukan looping terhadap variabel carts, lalu melakukan looping terhadap products untuk mendapatkan total harga dari jumlah pembelian yang dipilih.
"""


carts = []
while True :
    print("1. Melihat isi keranjang")
    print("2. Menambahkan isi keranjang")
    print("3. Menghitung total isi keranjang")
    print("4. Exit")	
    option = int(input("Pilih 1 - 4 : "))
    
    if option == 1:
        for product in carts:
            print(product)

    elif option == 2:
        name = input("Nama barang : ")
        qty = input("Jumlah barang : ")
        data = {"name": name, "quantity": int(qty)}
        carts.append(data)
        
    elif option == 3:
        for product in carts:
            name = product['name']
            qty = product['quantity']
            
            for total in products: 
                if name == total['name']:
                    price = total['price']
                    amount = price * qty
                    print(f"Barang yang dibeli adalah {name}, Jumlah {qty}, harga asli {price} ,total harga : {amount}")
                    break        
    elif option == 4 :
        print("Thank you for buying!")
        break