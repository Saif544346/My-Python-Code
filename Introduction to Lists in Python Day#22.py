l=[3,4,6,7,8,"saif",True]
print(l)
print(len(l))
print(l[3])
print(l[4])
print(l[5])
print(l[-3])
print(l[len(l)-3])
if 7 in l:
    print("yes")
else:
    print("no")
print(l)
print(l[1:5:2 ])
lst=[ i*i for i in range (10)]
print(lst)
lst=[i for i in range (20) if i%2==0]
print(lst)
lst=[i for i in range(30) if i%2==0+1]
print(lst)
