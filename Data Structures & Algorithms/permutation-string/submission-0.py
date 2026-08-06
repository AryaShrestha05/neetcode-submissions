class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Count frequencies of s1
        s1Count = {}
        for char in s1:
            s1Count[char] = s1Count.get(char, 0) + 1
        
        # Create a window of size len(s1) in s2
        windowCount = {}
        for i in range(len(s1)):
            char = s2[i]
            windowCount[char] = windowCount.get(char, 0) + 1
        
        # Check if window matches s1
        if windowCount == s1Count:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character on the right
            new_char = s2[i]
            windowCount[new_char] = windowCount.get(new_char, 0) + 1
            
            # Remove character on the left
            old_char = s2[i - len(s1)]
            windowCount[old_char] -= 1
            if windowCount[old_char] == 0:
                del windowCount[old_char]
            
            # Check if current window matches
            if windowCount == s1Count:
                return True
        
        return False
