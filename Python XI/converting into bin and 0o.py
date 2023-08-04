def convertbinoct(num, base=2):
    str1=''
    while num!=0:
        str1+=str(num%base)
        num//=base
    str1=str1[::-1]
    print(str1)

num=float(input("Enter the number which you want to convert to bin and oct : "))
convertbinoct(num)
convertbinoct(num, 8)
