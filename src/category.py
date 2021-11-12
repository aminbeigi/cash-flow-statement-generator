from month import Month

class Category:
    def __init__(self, category_type: str):
        self.category_type = category_type
        self.yearly_total = 0
        self.monthly_total = {i:0 for i in range(Month.JAN.value, Month.DEC.value+1)}

    def add(self, value: int, month: int):
        if value <= 0:
            raise ValueError("Transaction value must be greater than 0.")
        self.monthly_total[month] += int(value)
        self.yearly_total += int(value)

    def get_monthly(self) -> dict:
        return self.monthly_total

    def get_yearly(self) -> int:
        return self.yearly_total

    def __str__(self):
        return f'Category(category_type={self.category_type})'