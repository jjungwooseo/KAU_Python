count = int(input())
numbers = []
for _ in range(count):
    a = int(input())
    numbers.append(a)
numbers.sort()
for i in numbers:
    print(i)