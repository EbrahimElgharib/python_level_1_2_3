# Python Task Leve3 11 :
# 11. Make a temperature/measurement converter. Write a script that can convert Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different ways

import sys
        
# function of temperature converter
def temp_converter():
    while True:
        quest = input("To convert from F ---> C please enter 1\n To convert from C ---> F please enter 2\n To return or close this please enter other letter : ")
        if quest == '1':
            # from f to c
            f = float(input("Enter F temp to conver it : ")) #!!! need exception
            c = (f-32)*5/9
            print(f"F = {f} convert to C = {c} degrees")
            
        elif quest == '2':
            # from c to f
            c = float(input("Enter C temp to conver it : ")) #!!! need exception
            f = c * 9/5 + 32
            print(f"C = {c} convert to F = {f} degrees")
            
        else:
            return

# function of measurement converter
def measure_converter():
    while True:
        quest = input("To onvert from Inch ---> Cm please enter 1\n To convert from Cm ---> Inch please enter 2\n To return or close this please enter other letter : ")
        if quest == '1':
            # from Unch to cm
            i = float(input("Enter Inch measure to conver it : ")) #!!! need exception
            cm = (i-32)*5/9
            print(f"Inch = {i} convert to Cm = {cm}")
            
        elif quest == '2':
            # from Cm to Inch
            cm = float(input("Enter Cm to conver it : ")) #!!! need exception
            i = cm * 9/5 + 32
            print(f"Cm = {cm} convert to Inch = {i}")
            
        else:
            return

# main
print("#"*10+"   Hello Converters   "+"#"*10)
while True:
    converter = input("Enter Converter Type you need: Temperature/Measurement : Enter 1 if Temp or 2 if Measure or else if close : ")
    if converter == '1':
        temp_converter()
    elif converter == '2':
        measure_converter()
    else:
        print("#"*10+"   ByBy Converters   "+"#"*10)
        sys.exit()

