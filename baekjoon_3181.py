ignore = {'i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'}
words = input().split()
result = [words[0][0].upper()]
for word in words[1:]:
    if word not in ignore:
        result.append(word[0].upper())
print(''.join(result))