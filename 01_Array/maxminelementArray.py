# Size of array elements
n = int(input("Enter size of array:"))

# Integer inputs of array
print("Enter Array element:")
inp = []
for i in range(0,n):
    inp_element = int(input())
    inp.append(inp_element)
print("Entered array elements are: ",inp)

# max() used for find maximum value 
print("Maximum value is: ",max(inp))

# min() used for find minimum value
print("Minimum value is: ",min(inp))