import pickle

def create_pickle_file(file_name,data):
    with open(file_name,'wb')as file:
        pickle.dump(data,file)
    print("file successfully created...")
        
file_name = "pickle_file.ashish"
data = ["Ashish",31,"Yavatmal","15LPA"]
#create_pickle_file(file_name,data)

def read_pickle_file(file_name):
    with open (file_name,'rb')as file:
        data1 = pickle.load(file)
        return data1
        
var = read_pickle_file(file_name)
print(var)