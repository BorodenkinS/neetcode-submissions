from array import array

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        def countFreq(s):
            freq = [0 for _ in range(26)]
            for char in s:
                freq[ord(char) - ord('a')] += 1

            return tuple(freq)

        for s in strs:
            key = countFreq(s)
            if key in anagrams.keys():
                anagrams[key].append(s)
            else:
                anagrams.update({key: [s]})

        return list(anagrams.values())