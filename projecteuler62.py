from collections import defaultdict

cubes_dict = defaultdict(list)
n = 1
while True:
    cube = n**3
    canonical = "".join(sorted(str(cube)))  
    cubes_dict[canonical].append(cube)
    
    if len(cubes_dict[canonical]) == 5:
        print(min(cubes_dict[canonical]))
        break
    n += 1
