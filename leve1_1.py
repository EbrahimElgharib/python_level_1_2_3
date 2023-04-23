# Python Task Level 1 :
# 1. Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in the x,y range


# input x,y
while True:
    try:
        x, y = int(input("Please input two integer numbers: ")), int(input("Please input two integer numbers: "))
        print(x,y)
        break
    except Exception:
        print("Error: Please type again a valid integer number.")

# calculate even and odd numbers between range of x,y
even_list = []
odd_list = []

for n in range(x+1, y):
    if n%2 == 0: #even
        even_list.append(n)
    else: #odd
        odd_list.append(n)


# print lists
print(f"Even Numbers: {even_list}")
print(f"Odd Numbers: {odd_list}")
  
