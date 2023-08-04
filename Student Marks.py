M1=float(input("Enter the marks obtained in English (out of 100) :"))
M2=float(input("Enter the marks obtained in Language 2 (out of 100) :"))
M3=float(input("Enter the marks obtained in Science (out of 100) :"))
M4=float(input("Enter the marks obtained in Maths (out of 100) :"))
M5=float(input("Enter the marks obtained in Social (out of 100) :"))
M6=float(input("Enter the marks obtained in Computer Applications (out of 100) :"))
T=M1+M2+M3+M4+M5+M6
A=T/6       
print("Total Marks =", T)
print("Average =", A)
if M1 and M2 and M3 and M4 and M5 and M6 >= 32:
    print("You have been Passed")
if M1 <= 33:
    print("You have Failed in English")
if M2 <= 33:
    print("You have Failed in Language 2")
if M3 <= 33:
    print("You have Failed in Science")
if M4 <= 33:
    print("You have Failed in Maths")
if M5 <= 33:
    print("You have Failed in Social")
if M6 <= 33:
    print("You have Failed in Computer Applications")    
