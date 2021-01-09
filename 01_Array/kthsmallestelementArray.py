# Integer inputs in array
inp = [int(x) for x in input("Enter numbers: ").split()]
print("Entered array is:",inp)

# sort the array elements to find kth smallest element
inp.sort()
print("Sorted array is:",inp)

# kth smallest element
k = int(input("Enter key: "))
print("Kth element is:",inp[k-1])