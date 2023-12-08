def hello():
    print("Hello World")

hello()

# sebuah fungsi dapat memiliki parameter -> syarat
# ketika fungsi punya param, kita bisa kasih dia argumen (nilai yang diberikan ketika fungsi dipanggil)
def sayname(name):
    print(f"Hello, {name}!")

sayname("Dini")

n = "Dino"
sayname(n) # Argumen yang dilempar dari variabel n adalah "Dino"

def say(name, age):
    print(f"Hello, {name}! Your age is: {age}")

say("Dinot", 20)
a = "Dinai"
b = "19\n"
say(a, b,)

# nama fungsi lebih baik kata kerja, contoh: create, getByName, execute

## CLASS
# class -> kumpulan beberapa fungsi
class Message:
    def say_hello(self):
        print("Hello, Dinn!")

    def hello(self):
        self.say_hello()
        print("Ini dari fungsi hello")

    def hey(self):
        print("\nIni dari fungsi hey")
        self.hello() # manggil fungsi lain tapi bukan untuk diprint

msg = Message() #di inisiasi dan disimpan ke variabel bernama msg, jadi variabel ini adalah objek
msg.say_hello()
msg.hello()
msg.hey()

## METHOD CONSTRUCTOR
class pesan:
    def __init__(self):
        print("\nMethod constructor berjalan!\n\n") # bisa keprint padahal ga dipanggil pake alias

    def gojo(self):
        print("Ini gojo\n") # ini gaakan keprint kalo kita ga tambahin m.gojo()

m = pesan() # ini INISIASI
# Artinya method constructor akan berjalan pada saat class di-inisiasi. 
# Inget ya guys, pada saat inisiasi, artinya pada saat class tersebut dipanggil dengan buka kurung tutup kurung.


## MANFAAT METHOD CONSTRUCTOR
class Nama:
    def __init__(self):
        self.nama = "tidak ada nama"
        
    
    def say_name(self):
        print(f"Nama kamu adalah: {self.nama}")
    
    def change_name(self, name:str):
        self.nama = name # sekarang self.nama adalah Dini karena nilainya dioper/di-pass
        print(f"Sudah berhasil merubah nama, nama kamu saat ini: {self.nama}")
    
n = Nama()
n.change_name("Dini") # ngoper Dini ke param fungsi change_name, makanya namanya ganti. Pake self biar bisa interaksi
n.say_name()