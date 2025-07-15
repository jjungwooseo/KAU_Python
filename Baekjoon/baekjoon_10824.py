a,b,c,d = map(int,input().split())
str_a = str(a)
str_b = str(b)
str_ab = str_a + str_b
str_c = str(c)
str_d = str(d)
str_cd = str_c + str_d
str_ab = int(str_ab)
str_cd = int(str_cd)
print(str_ab + str_cd)