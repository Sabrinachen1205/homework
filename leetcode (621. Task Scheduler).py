class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter=Counter(tasks)
        collect=sorted(counter.values(), reverse=True)
        most=collect[0]
        numOfMost=collect.count(most)
        max_len=(most-1)*(n+1)+numOfMost
        return max(len(tasks), max_len)