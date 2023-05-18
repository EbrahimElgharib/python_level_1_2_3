# Python Task Leve3 10 :
# 10.Build a countdown calculator. Write some code that can take two dates as input, and then calculate the amount of time between them


import time


def count_down_calc(n_seconds):
    print("m : s")
    while n_seconds+1:
        mins, secs = n_seconds//60, n_seconds%60

        print(f"{mins} : {secs} ")
        time.sleep(1)
        n_seconds -= 1
        

# input number of Seconds to count down
while True:
    try:
        n_seconds = int(input("Please input integer Seconds : "))
        break
    except Exception:
        print("Error: Please type again a valid integer number.")

count_down_calc(n_seconds)
