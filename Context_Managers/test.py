class FileManager:
    def __init__(self,filename):
        self.filename = filename

    def __enter__(self):
        self.open_file = open(self.filename)
        return self.open_file

    def __exit__(self, *exc):
        self.open_file.close()

with FileManager('readme.txt') as file:
    text = file.read()
    print(text)