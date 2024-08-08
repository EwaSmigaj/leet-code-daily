import math


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.getBad(n, math.ceil(n/2))

    def getBad(self, end, l):
        if end == 1:
            return 1
        isBad = isBadVersion(l)
        if isBad is True:
            if l == 1:
                return l
            isPreviousBad = isBadVersion(l-1)
            if isPreviousBad is False:
                return l
            return self.getBad(l, math.ceil(l/2))
        return self.getBad(end, l + math.ceil((end-l)/2))


def isBadVersion(n, bad=1):
    if n >= bad:
        return True
    return False

