Sent=input("Enter a Sentence to Capitalize each word : ")
Edit=""
Replica=Sent.split(" ")

for x in Replica:
    Dup=list(x)
    
    if 97<=ord(Dup[0])<=122:
        Dup[0]=chr(ord(Dup[0])-32)

    for y in Dup:
            Edit+=y         
         
    Edit+=" "

print("The Original Sentence is : ", Sent)
print("The Sentence with each word Capitalized is :", Edit)



    
