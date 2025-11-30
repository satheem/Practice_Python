N = int(input("Enter a no: ")) + 1

for no in range(1,N):
    if (no % 3 == 0 or no % 5 == 0) and no % 15 != 0:
        print(no)