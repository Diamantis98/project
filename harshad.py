harshad = []
multiple = []
for i in range (1000) :
    b=str(i+1)
    list(b)
    sum=0
    mul=1
    for j in range (len(b)):
        sum = int(b[j])+sum
        mul = int(b[j])*mul
    if ((i+1) % sum) == 0 :
        harshad.append(i+1)
    if (mul != 0) :
        if ((i+1) % mul) == 0 :
            multiple.append(i+1)
print 'Harshad Numbers are : \n ', harshad
print  '\n Nubmers that their digits product can divide them are : \n ' ,multiple
