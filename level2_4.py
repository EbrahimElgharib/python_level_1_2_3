# Python Task Leve2 4 :
# 4. Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional programming]


Names = ['mahmoud','farida','ali','hassan','mohamed', 'khaled','taha', 'xyz']


# Normal list
new_names1 = []

for name in Names:
    #if name[0] == 't':
    if name.count('a') >= 2:
        new_names1.append(name)

print(new_names1)


# list comprehension
new_names2 = [ name for name in Names if name.count('a')>= 2]
print(new_names2)


# functional programming
# function
def func(name):
    if name.count('a') >= 2:
        return name

new_names3 = list(filter(func, Names))
print(new_names3)
