N = int(input("Enter a no: ")) + 1

# Numbers Divisible by (3 or 5) and not divide by 15
for no in range(1,N):
    if (no % 3 == 0 or no % 5 == 0) and no % 15 != 0:
        print(no)