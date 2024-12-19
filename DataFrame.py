dict1 = { 
'Name' : ['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'], 
'Marks' : [98, 89, 99, 87, 90, 83, 99], 
'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female'] 
        }

def marks_show(dict1):
    krisha_marks = dict1['Marks'][2]
    print("krisha marks is :", krisha_marks)

marks_show(dict1)

import pandas
def data_frame(di):
    data = pandas.DataFrame(di)
    print(type(data))
    print(data)
    
data_frame(dict1)


# convert dict into dataframe using pandas library
import json    
def sum_of_marks(di):
    data = pandas.DataFrame(di)
    
    # addition all value from cloumn
    total_marks = data['Marks'].sum()
    print("total marks is :",total_marks)
    
    # count of gender, department, etc then
    gender_count = data["Gender"].value_counts()
    print("gender count is :",gender_count)
    
    # perform some operation on perticular column (less than, greater than conditions)
    less_than_95 = data[data["Marks"]<95]
    print("name and gender have a marksis less than 95 :",less_than_95)
    print(less_than_95[["Name","Marks"]])
    
    # convert dataframe into json format
    json_data = less_than_95[["Name","Marks"]].to_json(orient = "records")
    print("json format data is :",json_data)
    
sum_of_marks(dict1)
'''Name     Marks  Gender
0  Priyang     98    Male
1   Aadhya     89  Female
2   Krisha     99  Female
3   Vedant     87    Male
4   Parshv     90    Male
5   Mittal     83  Female
6  Archana     99  Female'''