def number_to_pwr(number, p): 
    print(number)
    print(p)
    solution_num = number
    if p == 0:
        return 1
    if p == 1:
        return number
    for i in range(p-1):
        solution_num *= number
    return solution_num