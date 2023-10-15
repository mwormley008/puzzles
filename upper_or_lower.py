def solve(s):
    up_count = 0
    for x in [*s]:
        print(x)
        if x.isupper() == True:
            up_count += 1
    if up_count > len(s)//2:
        return s.upper()
    else:
        return s.lower()