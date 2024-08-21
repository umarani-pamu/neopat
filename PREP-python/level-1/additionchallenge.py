# You are using Python
def findSum(n):
    sum=0
    if 0 <= n <= 10000:
        for i in range(0,n+1):
            sum=sum+2**i
        i=i+1
    return sum
n=int(input())    
print(findSum(n))    
        