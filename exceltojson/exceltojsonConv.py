import pandas

excel_data_sheet = pandas.read_excel('Trxplore-dataset.xlsx', sheet_name='Sheet2')

json_str = excel_data_sheet.to_json()

with open('Trxplore-dataset.json', 'w') as json_file:
    json_file.write(json_str)
print('Excel Sheet to JSON:\n', json_str)