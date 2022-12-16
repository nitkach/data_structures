n = int(input())

acc = 1

for i in range(1, n + 1):
    acc *= (i + (i % 2)) / (i - (i % 2) + 1)

print(acc)