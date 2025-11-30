usr_in = input("Enter No Comma Separated: ").replace(" ","")
nums = usr_in.split(",")
nums = [x for x in nums if x.strip()]

total = 0
max_no = min_no = int(nums[0])
count_even = 0
count_no_avg = 0

for no in nums:
    no = int(no)

    # SUM
    total += no

    # Largest
    if max_no < no:
        max_no = no

    # Smallest
    if min_no > no:
        min_no = no
    
    # Even numbers count
    if no%2 == 0:
        count_even +=1
    
    # Numbers greater than average
average = total/len(nums)

for no in nums:
    no = int(no)
    if average < no:
        count_no_avg +=1
    

print(f"Sum: {total}")
print(f"Largest: {max_no}")
print(f"Smallest: {min_no}")
print(f"Even numbers count: {count_even}")
print(f"Numbers greater than average: {count_no_avg}")