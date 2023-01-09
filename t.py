import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
# Load the existing Excel file
wb = openpyxl.load_workbook('file.xlsx')

# Create a dataframe with some sample data
data = {'Col1': [1, 2, 3], 'Col2': [4, 5, 6], 'Col3': [7, 8, 9]}
df = pd.DataFrame(data)

# Get the existing sheet in the Excel file
ws = wb['Sheet1']

# Find the next empty row in the sheet
next_row = ws.max_row + 1

# Add the data to the sheet, starting at the next empty row
for r in dataframe_to_rows(df, index=False, header=False):
    ws.append(r)

# Save the changes to the Excel file
wb.save('file.xlsx')