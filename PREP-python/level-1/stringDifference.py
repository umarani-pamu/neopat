
string1=input()
string2=input()
count1=0
count2=0
for i in range (0,len(string1)):
    if string1[i]=="?" or string2[i]=="?":
        count1=count1+1
  
    elif string1[i] !=string2[i]:
        count1=count1+1
        count2=count2+1
  
print(count2,count1)        

