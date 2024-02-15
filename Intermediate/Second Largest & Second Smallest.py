Given=[14,25,67,55,32,31,98,73,21,59]
Max=Second_Max=0
Min=Second_Min=10000

for x in Given:
    if x>Max:
        Second_Max=Max
        Max=x

    elif Max>x>Second_Max:
        Second_Max=x

    else:
        pass

    if x<Min:
        Second_Min=Min
        Min=x

    elif Min<x<Second_Min:
        Second_Min=x

    else:
        pass
    
print("The Given List is : ", Given)
print("The Second Maximum Value in the List is : ", Second_Max)
print("The Second Minimum Value in the List is : ", Second_Min)
