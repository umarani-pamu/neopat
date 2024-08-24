def total_savings(n):
    initial=[1000, 1000]
    for i in range(2,n+1):
        current=initial[i-1]+initial[i-2]
        initial.append(current)
    return sum(initial)
n=int(input())
print(total_savings(n))