def cubepairs(string):
    numbers = list(map(int, string.split()))
    pairs=[(i, i**3) for i in numbers]
    return pairs    
string = input()
print(cubepairs(string))

"""pairs = []
    for i in numbers:
        cube = i ** 3
        pairs.append((i, cube))
"""        