def smallestDivisor(n):
    if n<=1:
        return None
    for i in range(2,n):
        if n%i==0:
            return i
    return n    
n=int(input())
print(smallestDivisor(n))