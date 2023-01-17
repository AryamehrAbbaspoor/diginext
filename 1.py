### Function: 
def Pull(x, y):
    while len(x) < y:
        x += x
    print(x[:y])

### Input: 
inputString = input("Enter String: ")
inputNum = int(input("Enter Number: "))

### Call Function: 
Pull(inputString, inputNum)

