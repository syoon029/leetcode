from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        count = Counter(nums)
        frequent = count.most_common(k)

        for i in frequent:
            result.append(i[0])

        return result
