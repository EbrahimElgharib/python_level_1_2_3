# Python Task Leve2 2 :
# 2. Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional programming]


Names = ['mahmoud','farida','ali','hassan','mohamed', 'khaled','taha', 'xyz']


# Normal list
new_names1 = []

for name in Names:
    if 'a' in name:
        new_names1.append(name)

print(new_names1)


# list comprehension
new_names2 = [ name for name in Names if 'a' in name]
print(new_names2)


# functional programming
# function
def func(name):
    if 'a' in name:
        return True

new_names3 = list(filter(func, Names))
print(new_names3)
