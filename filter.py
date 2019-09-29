lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(lst)

even=list(filter(lambda x:x%2==0,lst))
print(even)
even=tuple(filter(lambda x:x%2==0,lst))
print(even)
even=set(filter(lambda x:x%2==0,lst))
print(even)