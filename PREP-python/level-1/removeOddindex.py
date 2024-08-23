
def remove_odd_index(string):
    result=""
    for i in range(len(string)):
        if i%2==0:
            result=result+string[i]
    return result
string=input()
print(remove_odd_index(string))