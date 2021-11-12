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
    
    def __init__(self, category_type: str):
        self.category_type = category_type
        self.yearly_total = 0
        self.monthly_total = {i:0 for i in range(1,13)}

    def add(self, value: int, month: int):
        self.monthly_total[month] += int(value)
        self.yearly_total += int(value)

    def get_monthly(self) -> dict:
        return self.monthly_total

    def get_yearly(self) -> int:
        return self.yearly_total

    def __str__(self):
        return f'Category(category_type={self.category_type})'