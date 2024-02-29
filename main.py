class deBuLa3:
    def __init__(self, debul1, debul2, debul3, debul4):
        self.debul1 = debul1
        self.debul2 = debul2
        self.debul3 = debul3
        self.debul4 = debul4

    def __str__(self):
        return f"debul1: {self.debul1}\ndebul2: {self.debul2}\ndebul3: {self.debul3}\ndebul4: {self.debul4}"


OutCommand = deBuLa3("Мегачипс", "Dimooon", "matveeeeeeey", "Olesya")
print(OutCommand)