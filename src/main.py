import pandas as pd
from category import Category
from month import Month

"""
Simple script to extract monthly cash inflow and outflow via a transaction sheet.

format for excel file: [ date | (money inflow/outflow) | transaction ID | balance ]
"""

PATH_TO_TRANSACTION_DATA = "./data/transaction_data.xlsx"
DATE = 0
TRANSACTION_VALUE = 1
TRANSACTION_STR = 2
BALANCE = 3

def calculate_net(inflow: int, outflow: int) -> int:
    return inflow - outflow

def is_inflow(transaction_value: int) -> bool:
    return transaction_value > 0

def is_outflow(transaction_value: int) -> bool:
    return transaction_value < 0

if __name__ == '__main__':
    df = pd.read_excel(PATH_TO_TRANSACTION_DATA, header=None) # start reading from row 1
    inflow = Category("Inflow")
    outflow = Category("Outflow")
    # doesn't matter which order (ascd/desc)
    for index, row in df.iterrows():
        transaction_value = row[TRANSACTION_VALUE]
        if is_inflow(transaction_value):
            inflow.add(transaction_value, row[DATE].month)
        elif is_outflow(transaction_value):
            outflow.add(transaction_value*-1, row[DATE].month)
        else:
            raise ValueError("Transaction amount can not be 0.")

    monthly_inflow = inflow.get_monthly()
    yearly_inflow = inflow.get_yearly()
    monthly_outflow = outflow.get_monthly()
    yearly_outflow = outflow.get_yearly()

    data = [ ["Inflow"] + [total for total in monthly_inflow.values()] + [yearly_inflow],
            ["Outflow"] + [total for total in monthly_outflow.values()] + [yearly_outflow],
            ["Net"] + [calculate_net(monthly_inflow[index], monthly_outflow[index]) for index in range(Month.JAN.value, Month.DEC.value+1)] + [calculate_net(yearly_inflow, yearly_outflow)]
        ]
    
    df1 = pd.DataFrame(data, columns = ['Category', Month.JAN.name, Month.FEB.name, Month.MAR.name, Month.APR.name,
                                    Month.MAY.name, Month.JUN.name, Month.JUL.name, Month.AUG.name, Month.SEP.name,
                                    Month.OCT.name, Month.NOV.name, Month.DEC.name, 'Total'
                                    ])
    print(df1)
