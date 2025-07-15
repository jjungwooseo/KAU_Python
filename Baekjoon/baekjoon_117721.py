string = str(input())
for i in range(0,len(string),1):
    if  i % 9 == 0 and i!=0 :
        print(string[i])
    else:
        print(string[i],end='')

