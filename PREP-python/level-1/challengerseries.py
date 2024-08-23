
def WorL(string):
    wins=string.count('1')
    loses=string.count('0')
    if wins>loses:
        return "Win"
    else:
        return "Lose"
string=input()
print(WorL(string))
