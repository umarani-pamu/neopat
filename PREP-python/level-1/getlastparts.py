
def get_lastpart(string):
    if '/' in string:
        result1=string.rsplit('/',1)[0]
    if '-' in string:
        result2=string.rsplit('-',1)[0]
    return result1,result2    
string=input()
result_slash,result_dash=get_lastpart(string)
print(result_slash)
print(result_dash)