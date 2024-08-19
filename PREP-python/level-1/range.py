def test_range(number,n1,n2):
    if n1<= number <=n2:
        return "Inside"
    else:
        return "Outside"
n1=int(input())
n2=int(input())
number=int(input())
print(test_range(number,n1,n2))