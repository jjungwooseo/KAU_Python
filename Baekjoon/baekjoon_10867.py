count = int(input())
array = []
result = []
numbers = list(input().split())
for i in numbers:
    array.append(i)
for value in array:
    if value not in result:
        result.append(value)
result.sort()
for i in result:
    print(i,end=' ')



