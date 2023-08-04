B=input("Is the Compound Interest, Compounded Annually or Halfyearly or Quaterly ? ")
P=float(input("Enter the Principle Amount (in Rupees) ="))
R=float(input("Enter the Rate of Interest ="))
T=float(input("Enter the Time Period (in Years) ="))
C =P*(1+R/100)**T
if B=="Annually" or "annually" :
    A =P*(1+R/100)**T

if B=="Halfyearly" or "halfyearly" :
    A =P*(1+R/200)**2*T

if B=="Quaterly" or "quaterly":
    A =P*(1+R/400)**4*T
print("The Amount is =", C)
