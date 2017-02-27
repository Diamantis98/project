a=raw_input("Give a list separated with ',' : ")
a=a.split(",")
a=list(a)
print a
print type(a)
count=0
print "Length of list=" ,len(a)
while '0' in a:
    count=count+1
    a.remove('0')
print 'There are' , count, 'zero(s) in the list.'
for i in range(count):
    a.append('0')
print a
