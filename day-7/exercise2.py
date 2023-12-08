class Todo:
    def __init__(self):
        self.data = []

    def create(self, title:str, desc:str):
        list = {
            "title" : title,
            "desc" : desc
        }

        self.data.append(list)
    
    def read(self):
        for line in self.data:
            print(f"Title: {line['title']}")
            print(f"Description: {line['desc']}")
    
todo = Todo()
while True:
    title = input("What do you want to do: ")
    desc = input("Input description: ")

    todo.create(title, desc)
    todo.read()