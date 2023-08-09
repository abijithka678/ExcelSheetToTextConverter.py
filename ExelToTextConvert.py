import openpyxl

# Load the Excel spreadsheet
input_file_path = 'input.xlsx'
output_file_path = 'output.txt'

# Open the Excel file
workbook = openpyxl.load_workbook(input_file_path)
sheet = workbook.active

# Open the output file in write mode
with open(output_file_path, 'w') as output_file:
    # Iterate through rows in the Excel sheet
    for row in sheet.iter_rows():
        row_data = [cell.value for cell in row]
        row_str = '\t'.join(str(cell) for cell in row_data)  # Use tab as a separator
        output_file.write(row_str + '\n')

# Close the Excel file
workbook.close()

print(f"Data has been written to {output_file_path}")
