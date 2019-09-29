lst=[5,10,15,20]
print(lst)
from functools import reduce

vv=reduce(lambda x,y:x+x,lst)
print(vv)