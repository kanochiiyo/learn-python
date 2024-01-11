class Warehouse:
    def __init__(self):
        self.data = []
        self.current_number = 1  # Keep track of the current product number
        # kenapa self.current_number ada di __init__? supaya nilainya ga berubah tiap kali kita panggil fungsi create

    def create(self, name: str, stock: int):
        product = {
            "number": self.current_number,
            "name": name,
            "stock": stock
        }
        self.current_number += 1  # Increment the product number for the next product
        self.data.append(product)
    
    def read(self):
        os.system('clear')
        print("-------------------------------------------")
        print(f"{'No':<5} | {'Product Name':<25} | {'Stock':<5} |")
        print("-------------------------------------------")
        for item in self.data:
            product_number = f"{item['number']:<5} "
            product_name = f"| {item['name']:<25} "
            stocks = f"| {item['stock']:<5} |"
            print(product_number + product_name + stocks)
         #   print(f"{item['number']} | {item['name']}")
         #   print(f"Stock: {item['stock']}")
            
    def update(self, name: str, stock: int):
        for item in self.data:
            if item['name'] == name:
                item['stock'] = stock

    def delete(self):
        os.system('clear')
        optDel = input("Pilih nomor barang yang ingin didelete: ")
        optDel = int(optDel)
        self.data.pop(optDel - 1)
        self.current_number -= 1