x,y,z = input("Enter three number with spaces: ").split()
num_lis = [int(x),int(y),int(z)]

largest = smallest  = num_lis[0]
total = 0
triangle_typ = ""

for no in num_lis:
    # Largest
    if largest < no:
        largest = no
    # Smallest
    if smallest > no:
        smallest = no
    
# middle 
    total += no
middle = total-(largest+smallest)

if num_lis[0] == num_lis[1] == num_lis[2]:
    triangle_typ = "equilateral triangle"
elif num_lis[0] == num_lis[1] or num_lis[1] == num_lis[2] or num_lis[0] == num_lis[2]:
    triangle_typ = "isosceles triangle"
else:
    triangle_typ = "scalene triangle"
    
print(f"Largest: {largest}")
print(f"Middle: {middle}")
print(f"Smallest: {smallest}")
print(f"Triangle type: {triangle_typ}")