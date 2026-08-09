class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        if len(s1) > len(s2):
            return False

        s1dict = {}
        for i in range(len(s1)):
            s1dict[s1[i]] = s1dict.get(s1[i], 0) + 1

        s2dict = {}
        for j in range(len(s1)):
            s2dict[s2[j]] = s2dict.get(s2[j], 0) + 1

        if s1dict == s2dict:
            return True

        for k in range(len(s1), len(s2)):
            newChar = s2[k]
            s2dict[newChar] = s2dict.get(newChar, 0) + 1

            oldChar = s2[k - len(s1)]
            s2dict[oldChar] -= 1
            if s2dict[oldChar] == 0:
                del s2dict[oldChar]

            if s2dict == s1dict:
                return True
        
        return False