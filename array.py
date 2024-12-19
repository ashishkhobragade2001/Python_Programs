from array import array

# Create an integer array
int_array = array('i', [1, 2, 3, 4, 5])  # 'i' indicates integers

# Create a float array
float_array = array('f', [1.1, 2.2, 3.3, 4.4])  # 'f' indicates floats

# string array 
st_array = ["ashish","khobragade"]

# Display the arrays
print("Integer Array:", list(int_array))  # Convert to list for cleaner display
print("Float Array:", list(float_array))
print("string Array:", list(st_array))
