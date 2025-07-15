count = int(input())
for _ in range(count):
    alpabet = []
    string = input().split()
    for i in string:
        alpabet.append(i)
print(len(alpabet))
