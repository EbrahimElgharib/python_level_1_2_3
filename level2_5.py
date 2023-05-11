# Python Task Leve2 4 :
# 5. Print a list contains the len of each word in the list using [normal list - list comprehension - functional programming]


Names = ['mahmoud','farida','ali','hassan','mohamed', 'khaled','taha', 'xyz']


# Normal list
new_len1 = []

for name in Names:
        new_len1.append(len(name))

print(new_len1)


# list comprehension
new_len2 = [ len(name) for name in Names]
print(new_len2)


# functional programming
# function
def func(name):
        return len(name)

new_len3 = list(map(func, Names))
print(new_len3)
