#!/usr/bin/env/python 3.7

# fizz buzz using range and loops

value=int(input("Enter number of interations: "))

for counter in range(1,value+1):
    if counter%5==0 and counter %3==0:
        print("FizzBuzz")
    elif counter % 5 == 0:
        print("Fizz")
    elif counter % 3 == 0:
        print("Bizz")
    else:
        print(counter)
#
