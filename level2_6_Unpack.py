# Python Task Leve2 4 :
'''
6. Unpack the list in
7. a,b , a= the first index , b = rest of the list
8. a = the first index , b = the last index
9. a = the first index , b = the second index
'''



Names = ['mahmoud','farida','ali','hassan','mohamed', 'khaled','taha', 'xyz']


# 6. Unpack the list in
print("All Names: ",Names)

# 7. a,b , a= the first index , b = rest of the list
a, *b = Names
print("first index: ",a)
print("rest values: ",*b)

print('########################################')
# 8. a = the first index , b = the last index
a, *args, b  = Names
print("first index: ",a)
print("last index: ",b)

print('########################################')
# 9. a = the first index , b = the second index
a, b, *args = Names
print("first index: ",a)
print("second index: ",b)
