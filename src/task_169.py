from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsHash = Counter(nums)
        return max(numsHash, key=numsHash.get)
