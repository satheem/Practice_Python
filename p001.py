import numpy

def arrays(arr):
    # Convert input list to numpy array with float type
    arr = numpy.array(arr, float)
    # Reverse the array
    arr_reverse = arr[::-1]
    return arr_reverse

# Read input from user, split into a list
arr = input().strip().split(' ')
# Call the function
result = arrays(arr)
# Print the result
print(result)
