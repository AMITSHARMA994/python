#a=3
#('a',a,type(a))
#b=str(a)
#print('b',b,type(b))

#c=float(a)
# print(c)

f="30a"
print(type(int(f[0:2])),int(f[0:2]))

e="10.0"
print(int(float(e)))


l,t=50,90
l,t=90,50
print(l)
print(t)

j=70
k=40
temp=j+k
j=temp-j
k=temp-k
print(j)
print(k)