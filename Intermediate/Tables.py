Num=float(input("Enter a Number for which you want to create a table : "))
Fac=int(input("Enter a Number till which you want to create a table : "))
print("", end="\n\n")
for x in range(1, Fac+1):
	print(Num, "x", x, "=", Num*x, end="\n\n")

print("Thus we have printed the table for " + str(Num) + " till " + str(Fac) + " !!")
