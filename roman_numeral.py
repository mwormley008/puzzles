class Solution:
    def romanToInt(self, s: str) -> int:
        answer_sum = 0
        values_dict = {'I':1, 'V':5, 'X':10, 'L':50,
        'C':100,'D':500,'M':1000}
        for count, ele in enumerate(list(s)):
            if count+1 < len(list(s)):
                if values_dict[ele] < values_dict[list(s)[count+1]]:
                    answer_sum -=  values_dict[ele]
                else:
                    answer_sum += values_dict[ele]
        else:
            answer_sum += values_dict[ele]
        return answer_sum