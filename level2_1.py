# Python Task Leve2 1 :
# 1. Transform all names to uppercase using [normal list - list comprehension - functional programming]


Names = ['mahmoud','farida','ali','hassan','mohamed', 'khaled','taha']


# Normal list
new_names1 = []

for name in Names:
    new_names1.append(name.upper())

print(new_names1)


# list comprehension
new_names2 = [ name.upper() for name in Names]
print(new_names2)


# functional programming
# function
def func(name):
    return name.upper()

new_names3 = list(map(func, Names))
print(new_names3)
