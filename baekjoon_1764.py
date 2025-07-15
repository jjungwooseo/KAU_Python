a, b = map(int, input().split())
list_a = set(input() for _ in range(a))
list_b = set(input() for _ in range(b))

find_list = sorted(list_a & list_b)

print(len(find_list))
for name in find_list:
    print(name)