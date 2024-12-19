import pandas as pd

def get_total_books_count(url):
    
    data = pd.read_table(url, delimiter=",")  
    print(data)
    print("DataFrame shape:", data.shape)
    print("Columns in DataFrame:", data.columns)

    
    total_book = data.iloc[:, 2].count()
    print("total books is :",total_book)
    
    total_page_of_all_books = data.iloc[:,3].sum()
    print("total page of all books is: ",total_page_of_all_books)

## calling 
url = "https://public.karat.io/content/test/test_file.txt"
get_total_books_count(url)


##======================== when data are store in localy in string format then
import pandas as pd
from io import StringIO

# Define CSV data as a string
csv_data = '''   
379,Kelliann,attack of the killer bebes disneys kim possible 7,80
458,Courtnee,the star of melvin,32
558,Elysse,two moons in august,199
83,Kabir,chin chiang and the dragons dance,32
211,Coley,finishing becca,362
732,Tommy,counting to christmas,24
813,Donya,holes,233'''

# Define function to read the data
def read_data_from_csv(d):
    # Use StringIO to simulate a file-like object
    data = pd.read_csv(StringIO(d), delimiter=",", header=None)
    print(data)

# Call the function with the CSV string
read_data_from_csv(csv_data)