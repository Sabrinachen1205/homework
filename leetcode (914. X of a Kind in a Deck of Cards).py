class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        stat = collections.Counter(deck)
        for j in range(2, min(stat.values()) + 1):
            flag = True
            for val in stat.values():
                if val % j != 0:
                    flag = False
                    break
            if flag:
                return True
        return False