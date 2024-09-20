import itertools

elements = ['a', 'b', 'c', 'd']

r = 2  
combinations = list(itertools.combinations(elements, r))
for combo in combinations:
    print(combo)
