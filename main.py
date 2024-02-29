class deBuLa3:
    def __init__(self, debul1, debul2, debul3, umni1):
        self.debul1 = debul1
        self.debul2 = debul2
        self.debul3 = debul3
        self.umni1 = umni1

    def __str__(self):
        return f"debul1: {self.debul1}\ndebul2: {self.debul2}\ndebul3: {self.debul3}\numni1: {self.umni1}"


OutCommand = deBuLa3("Мегачипс", "Dimooon", "matveeeeeeey", "Olesya")
print(OutCommand)
