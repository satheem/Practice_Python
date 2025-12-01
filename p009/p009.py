usr_in = input("Enter numbers: ").replace(" ","").split(',')
usr_in = [int(N) for N in usr_in if N.strip()]
print(usr_in)

total = 0
largest = smallest = usr_in[0]
count_even = 0
count_avg = 0

for no in usr_in:
    # total
    total += no

    # Largest
    if largest < no:
        largest = no
    
    # Smallest
    if smallest > no:
        smallest = no
    
    # Even count
    if no % 2 == 0:
        count_even += 1

avg = total / len(usr_in)
# Greater than average count
for no in usr_in:
    if avg < no:
        count_avg += 1
    

print(f"total: {total}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Even count: {count_even}")
print(f"Greater than average: {count_avg}")

