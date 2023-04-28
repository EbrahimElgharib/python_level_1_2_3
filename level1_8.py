# Python Task Level, 1 :
# Create a function that takes x,y and prints all the number that can be divide by y from x to 100


# get two numbers x,y
while True:
    
    try:
        x, y = int(input("type number1: ")), int(input("type number2: "))
        break
        
    except Exception:
        print("try a valid int number please.")

    
# output
print("All numbers that can be divided on {y} from {x} to 100 :")
if x >= y:
    for n in range(x,101):
        if n%y == 0:
            print(n)
else:
    print("Nothing")

    
        
