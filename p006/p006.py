N = int(input("Enter a no: ")) + 1

for no in range(1,N):
    # Finding Odd No or Even No
    remainder = no % 2
    if remainder == 0:
        print(f"{no} Even")
    else:
        print(f"{no} Odd")
    