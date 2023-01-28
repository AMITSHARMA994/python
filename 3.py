print("hello world")
#TUPLE
a=tuple()
print(a)
a=(2,3,7,8)
print(a)
a=(2,3,7,8,"amit")
print(a)
a=a.index('amit')
print(a)
a=2,3,4
print(a)
print(type(a),id(a))
e=(2,3,5)
print(e)
print(e[0])

a=(3,5,6,7,8)
f,*d,e=a
print(f)
print(d)
print(e)