# You are using Python
def findType(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
        if count>4:
            return "Not Nice"
    return "Nice" if count==4 else "Not Nice"
ticket_number=int(input())
print(findType(ticket_number))
    