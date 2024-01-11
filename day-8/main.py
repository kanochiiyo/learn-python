from app.warehouse import Warehouse
import os
from time import sleep

warehouse = Warehouse()

while True:
    print("1. Tambah Barang")
    print("2. Lihat Barang")
    print("3. Update Stok Barang")
    print("4. Hapus Barang")
    print("5. Exit")
    opt = input(" >> ")

    if opt == "1":
        os.system('clear')
        amount = input("How much product you want to input: ")
        amount = int(amount)

        os.system("clear")
        for i in range(amount):
            name = input("Input product name: ")
            stock = input("Input the stock: ")
            stock = int(stock)

            warehouse.create(name, stock)
        os.system("clear")
    elif opt == "2":
        warehouse.read()
        sleep(3)
        os.system("clear")
    elif opt == "3":
        name = input("\nMasukkan nama barang: ")
        stock = input("Masukan stok update barang: ")
        stock = int(stock)

        warehouse.update(name, stock)
        print("Berhasil update stok!\n")
    elif opt == "4":
        warehouse.delete()
    elif opt == "5":
        print("Program akan keluar")
        sleep(2)
        exit()
    else:
        opt = input("Pilihan tidak valid.\n >> ")
