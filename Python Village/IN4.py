A = int(input("Input postive A integer:"))
B = int(input("Input postive B integer:"))
total = 0
for num in range(A, B):
    if num % 2 == 1:
        total += num

print(total)