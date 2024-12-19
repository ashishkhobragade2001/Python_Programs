import datetime


ob_date = datetime.datetime(2024,12,6,12,30,32)
print(ob_date)

## current date and time show 
current_date_time = datetime.datetime.now()
print(current_date_time)
## only show years
print("Year :",current_date_time.year)
## only show month
print("Month :",current_date_time.month)
## only show date 
print("Date :", current_date_time.day)

## today only date 
only_date = datetime.datetime.now().date()
print("only date : ",only_date)

## today only time 
only_time = datetime.datetime.now().time()
print("only time : ",only_time)

## =============================================================

from datetime import datetime

### strftime
ip_date = input("Enter date YYYY-MM-DD  :")
ob_date = datetime.strptime(ip_date, "%Y-%m-%d")
out_date = datetime.strftime(ob_date,"%d:%m:%Y")
print(out_date) #06:12:2055

##==================================================================
import datetime

print("tuday date is : ",datetime.date.today())

date_obj = datetime.date(2024,12,6)
print(date_obj)

## i want only year
print("only year : ", date_obj.year)

## only month
print("only month : ", date_obj.month)

# only day
print("only day : ", date_obj.day)

### format date object as a string 
any_date = datetime.date(2050,12,31)
str_obj = any_date.strftime("%Y-%m-%d")
print("string format :",str_obj)
print(type(str_obj))#class str

# convert str date into datetime format
date_datatype = datetime.datetime.strptime(str_obj, "%Y-%m-%d")
print("convert str date into date format :", date_datatype)
print(type(date_datatype))

