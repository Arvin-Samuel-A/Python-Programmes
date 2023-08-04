from random import randint as rint

Number=rint(10,50)

for x in range(5):
    Input=int(input("Enter a Number to Guess from 10 to 50 : "))

    if Input==Number:
        print("You have Won the Game !!!")
        break

    if x==3:
        print("Sorry you have Entered a Wrong Number. Try Again. Last chance !")
        print()
        continue

    if x==4:
        print()
        continue

    print("Sorry you have Entered a Wrong Number. Try Again. " + str(4-x) + " chances left !")
    print()

else:
    print("You have Lost the Game !!!")
    print("The Number was", Number)
