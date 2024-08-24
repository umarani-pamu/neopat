"""def smallest_bigger_stick_length(n, lengths):
    max_length = float('-inf')
    for i in range(n - 1):
        max_length = max(max_length, max(lengths[i], lengths[i + 1]))
    return max_length

N = int(input().strip())
lengths = list(map(int, input().strip().split()))
print(smallest_bigger_stick_length(N, lengths))
"""
n=int(input())
arr=[int(i) for i in input().split()][:n]
add=0
for i in range(0,n,2):
    if arr[i]<arr[i+1]:
        add+=arr[i]
    else:
        add+=arr[i+1]
print(add)