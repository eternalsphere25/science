import pandas as pd
import pyexcel_ods3

def find_empty_items_ods_raw(input_sheet):
    empty = []
    for x in range(len(input_sheet)):
        row = input_sheet[x]
        if len(row) == 0:
            empty.append(x)
    return empty

def generate_dataframe_from_ods_raw(input_data):
    dataframe = pd.DataFrame(input_data[1:], columns=[input_data[0][0], input_data[0][1], input_data[0][2], input_data[0][3]])
    return dataframe


#Set file to read
file_name = input('Input file: ')

#Import data (each page of the ods file is a dictionary item)
data = pyexcel_ods3.get_data(file_name)
sheets = list(data.keys())

print("\nDisplaying data from '" + str(file_name) + "':")
for item in range(len(sheets)):
    print("")
    print('Sheet #' + str(item+1) + ': ' + sheets[item])
    print(data[sheets[item]])

#Set data sheet
sheet = data['Sheet1']

#Find empty items (empty items separate each section)
empty = find_empty_items_ods_raw(sheet)

#Separate the data on the sheet into separate lists
element_data_rows = sheet[0:empty[0]]

#Assign each data list to a dataframe
df_elements = generate_dataframe_from_ods_raw(element_data_rows)

print(df_elements)

print("")
print(len(element_data_rows[0]))

test_list = []
for x in range(len(element_data_rows[0])):
    test_list.append()