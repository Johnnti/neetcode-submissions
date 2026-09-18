from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            c = tuple(sorted(strs[i]))
            if c in dic:
                dic[c].append(strs[i])
            else:
                dic[c] = [strs[i]]
        result = []
        for key,value in dic.items():
            result.append(value)
        return result