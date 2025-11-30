usr_in = int(input("Enter a No: "))
if usr_in > 0:
    print("Positive")
elif usr_in < 0:
    print("Negative")
else:
    print("Zero")

remainder_2 = usr_in % 2

if remainder_2 == 0:
    print("Even")
else:
    print("Odd")

remainder_5 = usr_in % 5

if remainder_5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")