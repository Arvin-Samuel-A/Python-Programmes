String=input("Enter a String to check whether it is a Palindrome ot not : ").lower()
Reverse=''
Length=len(String)+1

for x in range(-1, -Length, -1):
    Reverse+=String[x]
    
if Reverse==String:
    print("The Entered String of " + String + " is a Palindrome")

else:
    print("The Entered String of " + String + " is not a Palindrome")
