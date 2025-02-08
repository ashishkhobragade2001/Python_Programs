##@@@@@@@@@@@!!!!!!!!!!!dict methods and operations
menu = {}

## add element
menu["palak paneer"] = 120
menu["paneer tikka"] = 150
print(menu)

## access value of key of the element
paneer_tikka = menu["paneer tikka"]
print("get method :",menu.get("paneer tikka"))
print(paneer_tikka)

## remove palak paneer
del menu["palak paneer"]
print(menu)

## clear dictionary
#menu.clear()
print("clear dict :",menu)

## total lenght
print(len(menu))

## remove last element of dict
di = {"name":"ashish","age":30,"city":"yavatmal","bg":"o+"}
#di.popitem()
print(di)

## remove specific element from dict
#di.pop("city")
print("pop method is used :",di)
del di["city"]
print("using del method : ",di)

## all key in dict
for key in di:
    print(key)
## also
for key in di.keys():
    print(key)
    
## all values
for val in di.values():
    print(val)
    
## key,val  show
for k,v in di.items():
    print(k,v)
    
########################################################################  
## merge dict
menu.update(di)
print(menu)

## this also works
di = {2:10,3:30}
di2= {4:40,5:50}
print(di | di2)

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
sub_dict = {"state":{"MH":"mumbai", "UP":"Lakh9","BH":"bhopal"},
            "country":{"IND":"DEL","PAK":"ISLBD"}
          }
#print(sub_dict["state"]["MH"])# mumbai

#print({x:x**2 for x in range(21,31)})

## convert list to dict
name = ["ashish","rajesh","shiva"]
city = ["ytl","goa","pune"]
new_dict = dict(zip(name, city))
print(new_dict)

## convert list to each 
ashish_di = dict.fromkeys(name,city)
print(ashish_di)
##################################################################
di = {"ashish":30,
"ramesh":65,
"nagesh":55,
"brijesh":10,
   }

#print age grater than 50
var = {k:v for k,v in di.items() if v>50}
print(var)

############################
## sorted dict according to age in descending order 
print(dict(sorted(di.items(),key=lambda x:x[1], reverse = True)))





