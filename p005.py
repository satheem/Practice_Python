a, b, c = input("Enter 3 Numbers with space: ").split()
num_lis = [int(a), int(b), int(c)]

largest = smallest = num_lis[0]
is_posi = "No"
is_valid = "No"
for no in num_lis:
    # Largest
    if largest < no:
        largest = no
    # Smallest
    if smallest > no:
        smallest = no
    # Is positive 
    if no > 0:
        is_posi = "Yes"
    # Is valid triangle
    if int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a):
        is_valid = "Yes"

print(f"Largest {largest}")
print(f"Smallest {smallest}")
print(f"All positive {is_posi}")
print(f"Valid triangle {is_valid}")
      
