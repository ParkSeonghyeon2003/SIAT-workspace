class MyFolder:
    def __init__(self, files) -> None:
        self.files = files
    
    def __iter__(self):
        print("__iter__")
        for file in self.files:
            yield f"Processing... {file}"

folder = MyFolder(["doc1.pdf", "image.jpg", "data.csv"])

for f in folder:
    print(f)