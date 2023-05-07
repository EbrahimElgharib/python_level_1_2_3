# Python Task Leve2 3 :
# 3. Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional programming]


Names = ['mahmoud','farida','ali','hassan','mohamed', 'khaled','taha', 'xyz']


# Normal list
new_names1 = []

for name in Names:
    #if name[0] == 't':
    if name.startswith('t'):
        new_names1.append(name)

print(new_names1)


# list comprehension
new_names2 = [ name for name in Names if name.startswith('t')]
print(new_names2)


# functional programming
# function
def func(name):
    if name.startswith('t'):
        return name

new_names3 = list(filter(func, Names))
print(new_names3)
