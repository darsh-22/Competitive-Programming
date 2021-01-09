# function for reverse the inputed array
def rev_array(inp,start,end):
    while start < end:
        inp[start], inp[end] = inp[end] ,inp[start]
        start += 1
        end -= 1

# size of array
n = int(input("Enter size of array:"))

# user input array
print("Enter Array element:",end=" ")
inp = []
for i in range(0,n):
    inp_element = int(input())
    inp.append(inp_element)
print("Entered array elements are: ",inp)
# Output:- Entered array elements are:  [1, 2, 3, 4]


# function calling
rev_array(inp,0,n-1)

# Output:- Reversed array elements are:  [4, 3, 2, 1]
print("Reversed array elements are: ",inp)

# For python3 user we can also use list slicig method to reverse array elements

# reverse_array = inp[::-1]
# print("Reverse array elements are: ",reverse_array)
