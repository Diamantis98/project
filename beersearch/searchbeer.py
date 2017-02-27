import json

def countWord(word,needle):
    numWord = 0

    for i in range(1, len(word)-1):
        if word[i-1:i+(len(needle)-1)] == needle :
            numWord += 1
    return numWord


from pprint import pprint
with open('beers.json') as data_file:
    data = json.load(data_file)
needle=raw_input('Give characteristics of the beer you like separated with "," : ')
needle=needle.split(",")
needle=list(needle)
results=[]
for i in range (len(needle)) :
    for j in range (170):
        if i == 0 :
            results.append(0)
        test=data["data"][j]["description"]
        temp=countWord(test,needle[i])
        if temp > 0 :
            results[j]=results[j]+temp
m=max(results)
position=[i for i, j in enumerate(results) if j == m]
for i in range (len(position)):
    print 'We recomment you :' , data["data"][i]["name"] , '. With id :', data["data"][position[i]]["id"]
