a=dict()
print(a)
b={1:"rohan",2:"amit",3:"ashok"}
print(b[2])
b[2]="rohan"
print(b)
print(b.keys())
print(b.values())
print(b.get(2))
print(b.items())
b.update({4:"rahul"})
print(b)
b.popitem()
print(b)
b.popitem()
print(b)
b.setdefault(3)
print(b)
b[1]="rohan","sumit","kumar"
f={1:{"name":"rohan","father":"sumit","mother":"kumar"}
,2:{"name":"rohan","father":"amar","mother":"saroj"}}
print(f)
g=f[2]['father']
print(g)
