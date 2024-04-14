class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = s
        str = str.strip()
        
        if not str:
            return 0
        
        rstr = re.findall(r"^[+-]?\d+",str)
        if not rstr:
            return 0
        
        maxN = math.pow(2,31)-1
        minN = -(math.pow(2,31))
        if int(rstr[0]) > maxN:
            return int(maxN)
        elif int(rstr[0]) < minN:
            return int(minN)
        else:
            return int(rstr[0])