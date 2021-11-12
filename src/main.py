import pandas as pd
from category import Category

"""
Simple script to extract monthly cash inflows and outflows from a transaction sheet.

Format: Date | (money inflow/outflow) | Transaction ID | Balance
"""

PATH_TO_TRANSACTION_DATA = "./data/transaction_data.xlsx"
DATE = 0
TRANSACTION_AMOUNT = 1
TRANSACTION_STR = 2
BALANCE = 3

def calculate_net(inflow: int, outflow: int) -> int:
    return inflow - outflow

if __name__ == '__main__':
    df = pd.read_excel(PATH_TO_TRANSACTION_DATA)
    inflow = Category("Inflow")
    outflow = Category("Outflow")
    # doesn't matter which order (ascd/desc)
    for index, row in df.iterrows():
        if row[TRANSACTION_AMOUNT] > 0:
            inflow.add(row[TRANSACTION_AMOUNT], row[DATE].month)
        elif row[TRANSACTION_AMOUNT] < 0:
            outflow.add(row[TRANSACTION_AMOUNT]*-1, row[DATE].month)
        else:
            raise ValueError("Transaction amount can not be 0.")
    print(inflow)
    # print out monthy outflows and inflow
    monthly_inflow = inflow.get_monthly()
    yearly_inflow = inflow.get_yearly()
    monthly_outflow = outflow.get_monthly()
    yearly_outflow = outflow.get_yearly()

    d = [ ["Inflow"] + [total for total in monthly_inflow.values()] + [yearly_inflow],
            ["Outflow"] + [total for total in monthly_outflow.values()] + [yearly_outflow],
            ["Net"] + [calculate_net(monthly_inflow[index], monthly_outflow[index]) for index in range(1,13)] + [calculate_net(yearly_inflow, yearly_outflow)]
        ]
    
    df = pd.DataFrame(d, columns = ['Category', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Total'])
    print(df)