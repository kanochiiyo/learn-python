class Warehouse:
    def __init__(self):
        self.data = []

    def create(self, name: str, stock: int):
        product = {
            "name" : name,
            "stock" : stock
        }

        self.data.append(product)
    
    def read(self):
        for item in self.data:
            print("\n---------------------------------")
            print(f"Product: {item['name']}")
            print(f"Stock: {item['stock']}")
            print("--------------------------------\n")

warehouse = Warehouse()
while True:
    name = input("input product name: ")
    stock = input("input the stock: ")
    stock = int(stock) # Kita ubah stok dari string menjadi integer karena default input adalah string

    warehouse.create(name, stock)
    warehouse.read()