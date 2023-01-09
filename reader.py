import pandas as pd
FILENAME = 'Data.xlsx'
# Load a specific set of rows from the Excel file
# df = pd.read_excel(FILENAME, sheet_name='Data')
# for index, row in df[1:].iterrows():
#     print(row[0])
def get_column_count()->int:
    df = pd.read_excel(FILENAME, sheet_name='Data')
    return len(df.columns)
def get_all()->list:
    df = pd.read_excel(FILENAME, sheet_name='Data')
    results = [row[1] if row[2]=="A" else None  for index, row in df[1:].iterrows()]
    return results        
def get_active()->list:
    df = pd.read_excel(FILENAME, sheet_name='Data')
    results = [row[1] for index, row in df[1:].iterrows() if row[2]=="A"]
    return results

def get_failed()->list:
    df = pd.read_excel(FILENAME, sheet_name='Data')
    results = [row[1] for index, row in df[1:].iterrows() if row[2]=="F"]
    return results    