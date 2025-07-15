numbers = []
even = []
result = 0
for _ in range(7):
    a = int(input())
    numbers.append(a)
for i in numbers:
    if i % 2 == 1:
        even.append(i)
even.sort()
if len(even) == 0:
    print(-1)
else:
    print(sum(even))
    print(even[0])

