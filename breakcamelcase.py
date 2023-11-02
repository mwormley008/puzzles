# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
# Break camelCase
# converts camelCase into regular strings
def solution(s):
    solution_list = []
    for i in [*s]:
        if i.isupper() == True:
            solution_list.append(' '+i)
        else:
            solution_list.append(i)
    return ''.join(solution_list)