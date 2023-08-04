Sent=input("Enter the Sentence to find out the different characters present in it : ")
Upper=Lower=Digit=Others=Space=0

for x in Sent:
    if x.isupper():
        Upper+=1
    elif x.islower():
        Lower+=1

    elif x.isdigit():
        Digit+=1

    elif x.isspace():
        Space+=1
        
    else:
        Others+=1

print("The Number of Upper case Letters : ", Upper)
print("The Number of Lower case Letters is : ", Lower)
print("The Number of Digits is : ", Digit)
print("The Number of Alphabets is : ", Upper+Lower)
print("The Number of Spaces in the entered sentence is : ", Space)
print("The Number of Other Characters is : ",  Others)

        
