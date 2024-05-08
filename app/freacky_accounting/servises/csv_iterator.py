import csv

class CSVFileIterator:
    "Just for iter by file :)"
    def __init__(self, filename):
        self.filename = filename
        self.rows = None
    
    def __iter__(self):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            self.rows = list(reader)
        return iter(self.rows)
    
    def __getitem__(self, key):
        if isinstance(key, int):
            if self.rows is None:
                with open(self.filename, 'r', newline='') as file:
                    reader = csv.reader(file)
                    self.rows = list(reader)
            return self.rows[key]
        elif isinstance(key, slice):
            if self.rows is None:

                with open(self.filename, 'r', newline='') as file:
                    reader = csv.reader(file)
                    self.rows = list(reader)
            return self.rows[key]
        else:
            raise TypeError()

