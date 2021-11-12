class Category:
    # TODO: replace with built-in consts?
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12
    
    def __init__(self, name: str):
        self.name = name
        self.total = 0
        self.monthly_total = {i:0 for i in range(1,13)}

    def add(self, value: int, month: int):
        self.monthly_total[month] += value
        self.total += value

    def __str__(self):
        return f'Category(name={self.name})'