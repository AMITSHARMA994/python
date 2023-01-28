b=[2,3,4,5]
a,b,r,e=b
print(a)
print(b)
print(r)
print(e)

#unpacking
k=[50]
l=60
m=40
j=[k,l,m]
print(j)


a,d,f,g=(2,3,5,6)
print(a)
print(d)
print(f)
print(g)
#packing
k=(a,d,f,g)
print(k)

a={1,1,2,3}
print(a)
b,m,h=a
print(b)
print(m)
print(h)
k=1
m=1
n=2
f=3
j={k,m,n,f}
print(j)
b,m,*h={1,2,3,4}
print(b)
print(m)
print(h)

