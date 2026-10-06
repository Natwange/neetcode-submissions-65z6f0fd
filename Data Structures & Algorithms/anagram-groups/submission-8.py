from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        array_to_word = defaultdict(list)

        for word in strs:
            sig = [0] * 26
            for c in word:
                sig[ord(c) - ord('a')] += 1
            array_to_word[tuple(sig)].append(word)

        return list(array_to_word.values())
