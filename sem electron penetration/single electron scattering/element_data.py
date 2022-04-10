import pandas as pd
import pyexcel_ods3


class Element:
    def __init__(self, symbol, z, amu, density):
        self.symbol = symbol
        self.z = z
        self.amu = amu
        self.density = density


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

def lookup_element(input_element):
    #Set file to read
    file_name = "Element List.ods"

    #Import data (each page of the ods file is a dictionary item)
    data = pyexcel_ods3.get_data(file_name)
    sheets = list(data.keys())

    #print("\nDisplaying data from '" + str(file_name) + "':")
    #for item in range(len(sheets)):
    #    print("")
    #    print('Sheet #' + str(item+1) + ': ' + sheets[item])
    #    print(data[sheets[item]])

    #Set data sheet
    sheet = data['Sheet1']

    #Find empty items (empty items separate each section)
    empty = find_empty_items_ods_raw(sheet)

    #Separate the data on the sheet into separate lists
    element_data_rows = sheet[0:empty[0]]

    #Assign each data list to a dataframe
    df_elements = generate_dataframe_from_ods_raw(element_data_rows)

    #Extract headers from dataframe
    headers_list = []
    for x in range(len(element_data_rows[0])):
        headers_list.append(element_data_rows[0][x])

    #Lookup element name input by user
    selected_element = df_elements[df_elements['Element'] == input_element]

    #Return parameters as an object
    element = Element(
        selected_element[headers_list[0]].values[0],
        selected_element[headers_list[1]].values[0],
        selected_element[headers_list[2]].values[0],
        selected_element[headers_list[3]].values[0]
    )
    return element