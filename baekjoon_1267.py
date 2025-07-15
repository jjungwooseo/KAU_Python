price = []
young = 0
min = 0
count = int(input())
numbers = list(input().split())

for i in numbers:
    price.append(int(i))

for i in range(len(price)):
    young += (price[i] // 30 + 1) * 10
for j in range(len(price)):
    min += (price[j]// 60 + 1 ) * 15
if young > min :
    print(f'M {min}')
elif young < min :
    print(f'Y {young}')
else:
    print(f'Y M {young}')