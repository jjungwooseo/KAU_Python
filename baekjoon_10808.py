name = str(input())
alphabet = []
english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,len(name),1):
    alphabet.append(name[i])
for i in range(0,len(alphabet),1):
    for j in range(0,len(english),1):
        if alphabet[i] == english[j]:
            numbers[j] +=1
for i in numbers:
    print(i,end=' ')

