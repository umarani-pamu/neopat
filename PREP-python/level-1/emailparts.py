#importing regular expression 
import re
email=input()
pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
result=re.findall(pattern, email, flags=re.I)
for i in result:
    print(*i)