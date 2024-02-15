A=float(input("Enter the Value of Side of Cube (in Cms) :"))
CSA1=4*A**2
TSA1=6*A**2
print("The Lateral Surface Area of Cube of Side " + str(A) + " is (in Cm^2) = ", CSA1)
print("The Total Surface Area of Cube of Side " + str(A) + " is (in Cm^2) = ", TSA1)

L=float(input("Enter the Value of Length of Cuboid (in Cms) :"))
B=float(input("Enter the Value of Breadth of Cuboid (in Cms) :"))
H=float(input("Enter the Value of Height of Cuboid (in Cms) :"))
CSA2=2*(L+B)*H
C=(L*B)+(B*H)+(H*L)
TSA2=B*2
print("The Lateral Surface Area of Cuboid of Length " + str(L) + " , Breadth " + str(B) + " and Height " + str(H) + " is (in Cm^2) = ", CSA2)
print("The Total Surface Area of Cuboid of Length " + str(L) + " , Breadth " + str(B) + " and Height " + str(H) + " is (in Cm^2) = ", TSA2)
