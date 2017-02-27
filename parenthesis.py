a=raw_input('Give a sequence of parentheses: ')
a=list(a)
print a
suml=0
sumr=0
flag=0
for i in range(len(a)) :
    if a[i] == '(':
        suml=suml+1
    elif a[i] == ')':
        sumr=sumr+1
    else :
        print 'Wrong sequence!'
        flag = 2
        break
    if a[0] == ')' or a[len(a)-1] == '(':
        flag=1
    if sumr > suml :
        flag = 1
if flag == 0:
    if suml == sumr :
        print 'True'
    else:
        print 'False'
elif flag == 1:
    print 'False'
