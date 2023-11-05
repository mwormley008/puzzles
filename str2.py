class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not all(strs):
            return ''
        shrinking_circle = list(min(strs, key=len))
        for i in strs:
            for count, ele in enumerate(list(i)[:len(shrinking_circle):]):
                print(count)
                print(ele)
                if ele != shrinking_circle[count]:
                    shrinking_circle = shrinking_circle[:count:]
                    print(shrinking_circle)
                    if shrinking_circle == []:
                        return ''
                    break
            if shrinking_circle == '':
                return ''
        return ''.join(shrinking_circle)