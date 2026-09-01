from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for items in strs:
            anagram[tuple(sorted(items))].append(items)

        return list(anagram.values())
