def rev_array(inp,start,end):
    while start < end:
        inp[start], inp[end] = inp[end] ,inp[start]
        start += 1
        end -= 1
n = int(input("Enter size of array:"))
print("Enter Array element:",end=" ")
inp = []
for i in range(0,n):
    inp_element = int(input())
    inp.append(inp_element)
print("Entered array elements are: ",inp)
# reverse_array = inp[::-1]
# print("Reverse array elements are: ",reverse_array)      
rev_array(inp,0,n-1)
print("Reversed array elements are: ",inp)