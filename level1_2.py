# Python Task Level, 1 :
# Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can be divided on x,y


# get two numbers x,y
while True:
    
    try:
        x, y = int(input("type number1: ")), int(input("type number2: "))
        break
        
    except Exception:
        print("try a valid int number please.")

    
# output
print("All numbers that can be divided on {x} and {y} :")
for n in range(1,101):
    if n%x == 0 and n%y == 0:
        print(n)

    
        
