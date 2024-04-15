class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dict = {'Q':1, 'W':1, 'E':1, 'R':1, 'T':1, 'Y':1, 'U':1, 'I':1, 'O':1, 'P':1, 
               'A':2, 'S':2, 'D':2, 'F':2, 'G':2, 'H':2, 'J':2, 'K':2, 'L':2,
               'Z':3, 'X':3, 'C':3, 'V':3, 'B':3, 'N':3, 'M':3}
        ans = []
        flag = False
        
        for word in words:
            row = 0
            for index in range(len(word)):
                if len(word) == 1:
                    flag = True
                    
                if row != 0:
                    if row == dict[word[index].upper()]:
                        flag = True
                        continue
                    else:
                        flag = False
                        break
                else:
                    row = dict[word[index].upper()]
            
            if flag:
                ans.append(word)
            
        return ans