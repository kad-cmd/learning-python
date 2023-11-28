import random as digit

a = digit.randint(1,20)
b = digit.randint(1,20)
c = digit.randint(1,20)

if a > b and c:
    print(f"{a} is the largest digit")
elif b > c and a:
    print(f"{b} is the largerst digit")
else:
    print(f"{c} is the largest digit")