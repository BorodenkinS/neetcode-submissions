class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums_set = set(nums)
        seqs = dict()

        for num in nums_set:
            if num - 1 not in nums_set:
                seqs.update({num: 1})
        
        max_len = 1
        for start in seqs.keys():
            counter = start
            while counter + 1 in nums_set:
                counter += 1
                seqs[start] += 1
            if seqs[start] > max_len:
                max_len = seqs[start]

        return max_len
