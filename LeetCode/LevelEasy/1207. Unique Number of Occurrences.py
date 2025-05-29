from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            dic[i] = dic.get(i, 0) + 1

        list1 = list(dic.values())
        return True if len(list1) == len(set(list1)) else False
