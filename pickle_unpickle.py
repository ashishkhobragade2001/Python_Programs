import pickle 

def create_pickle_file(filename,data):
    with open (filename ,"wb") as file:
        pickle.dump(data, file)
    print("file has been created..")
    
filename = "Ashish.pkl"
data = {"name":["Ram","Shyam","Sita"],
"age":[40,45,30],
"gender":["M","M","F"]
}
#create_pickle_file(filename, data)

def read_pickle_file(filename):
    with open (filename,"rb") as file:
        pickle_data = pickle.load(file)
    print("unpickle data :\n", pickle_data)
    
read_pickle_file("ashish.pkl")