import pandas as pd
from category import Category

"""
Simple script to extract monthly cash inflows and outflows from a transaction sheet.

Format: Date | (money inflow/outflow) | Transaction ID | Balance
"""

PATH_TO_TRANSACTION_DATA = "./data/transaction_data_1.xlsx"
DATE = 0
TRANSACTION = 1
TRANSACTION_STR = 2
BALANCE = 3

if __name__ == '__main__':
    df = pd.read_excel(PATH_TO_TRANSACTION_DATA)
    # doesn't matter which order (ascd/desc)
    for index, row in df.iterrows():
            #if row[TRANSACTION] > 0:
            print()
