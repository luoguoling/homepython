__author__ = 'Administrator'
import os
for num in xrange(1,10):
    if num == 1:continue
    if num == 2:continue
    if num == 3:continue
    print num
    break

values = 1,2,3
print values
x,y,z = values
print x,y,z
t = 3
t *= 2
print t
mylist = ['item']
assert len(mylist) >= 1
mylist.pop()
#assert len(mylist) >= 1
names = ['x','y']
age = [3,5]
attr = zip(names,age)
print attr
for name,age in attr:
    print name,age

strings = ['2','1','1','2']
index = 0
for string in strings:
    print string
    if '2' in  string:
        strings[index] = '1'
#        print index
    index += 1
    print index
    print strings

zz = []
for x1 in range(2):
    for y1 in range(2):
         zz.append((x1,y1))
print zz
print [(m,n) for m in range(2) for n in range(3) ]
print  os.listdir('C://')
